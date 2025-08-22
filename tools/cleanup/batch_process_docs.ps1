#!/usr/bin/env pwsh
<#
.SYNOPSIS
    Batch process Cascadeur API documentation files with LLM cleaning
.DESCRIPTION
    Robust PowerShell script to clean markdown documentation using LiteLLM
    with error handling, progress tracking, and resume capability
.PARAMETER ApiKey
    API key for the LLM service (optional - will read from .api_key file or env var if not provided)
.PARAMETER BaseUrl
    Base URL for the LLM service (e.g., https://yunwu.ai/v1)
.PARAMETER Model
    Model name to use (default resolution: param > env CUSTOM_LLM_MODEL > .api_model_name > gpt-5)
.PARAMETER SourceDir
    Directory containing markdown files to process
.PARAMETER MaxRetries
    Maximum connection-related retries per file (default: 5). Non-transient errors won't be retried.
.PARAMETER ContinueOnError
    Continue processing even if files fail (default: true)
#>

param(
    [Parameter(Mandatory=$false)]
    [string]$ApiKey,
    
    [Parameter(Mandatory=$false)]
    [string]$BaseUrl,
    
    [Parameter(Mandatory=$false)]
    [string]$Model,
    
    [Parameter(Mandatory=$false)]
    [string]$SourceDir = "casey-docs\markdown",
    
    [Parameter(Mandatory=$false)]
    [int]$MaxRetries = 5,
    
    [Parameter(Mandatory=$false)]
    [switch]$ContinueOnError = $true,
    
    [Parameter(Mandatory=$false)]
    [string]$StateFile = "tmp\cleanup\ps_batch_state.json"
)

# Load API key from various sources if not provided
if (-not $ApiKey) {
    # Try to load from .api_key file first
    $apiKeyFile = Join-Path $PSScriptRoot ".api_key"
    if (Test-Path $apiKeyFile) {
        $ApiKey = (Get-Content $apiKeyFile -Raw).Trim()
        Write-Host "Loaded API key from .api_key file" -ForegroundColor Green
    }
    # Try environment variable
    elseif ($env:CUSTOM_LLM_API_KEY) {
        $ApiKey = $env:CUSTOM_LLM_API_KEY
        Write-Host "Loaded API key from environment variable" -ForegroundColor Green
    }
    else {
        Write-Host "ERROR: No API key provided!" -ForegroundColor Red
        Write-Host ""
        Write-Host "Please provide API key using one of these methods:" -ForegroundColor Yellow
        Write-Host "  1. Create tools\cleanup\.api_key file with your key"
        Write-Host "  2. Set environment variable: `$env:CUSTOM_LLM_API_KEY = 'your-key'"
        Write-Host "  3. Pass as parameter: -ApiKey 'your-key'"
        Write-Host ""
        exit 1
    }
}

# Load Base URL if not provided (order: param > .api_base_url file > env CUSTOM_LLM_BASE_URL)
if (-not $BaseUrl -or $BaseUrl -eq "") {
    $baseUrlFile = Join-Path $PSScriptRoot ".api_base_url"
    if (Test-Path $baseUrlFile) {
        $BaseUrl = (Get-Content $baseUrlFile -Raw).Trim()
        Write-Host "Loaded Base URL from .api_base_url file" -ForegroundColor Green
    } elseif ($env:CUSTOM_LLM_BASE_URL) {
        $BaseUrl = $env:CUSTOM_LLM_BASE_URL
        Write-Host "Loaded Base URL from environment variable" -ForegroundColor Green
    } else {
        Write-Host "ERROR: No Base URL provided!" -ForegroundColor Red
        Write-Host "Create tools\cleanup\.api_base_url or set CUSTOM_LLM_BASE_URL or pass -BaseUrl" -ForegroundColor Yellow
        exit 1
    }
}

# Resolve Model if not provided (order: param > env CUSTOM_LLM_MODEL > .api_model_name file > default 'gpt-5')
if (-not $Model -or $Model -eq "") {
    if ($env:CUSTOM_LLM_MODEL) {
        $Model = $env:CUSTOM_LLM_MODEL
        Write-Host "Loaded Model from environment variable" -ForegroundColor Green
    } else {
        $modelFile = Join-Path $PSScriptRoot ".api_model_name"
        if (Test-Path $modelFile) {
            $Model = (Get-Content $modelFile -Raw).Trim()
            Write-Host "Loaded Model from .api_model_name file" -ForegroundColor Green
        } else {
            $Model = 'gpt-5'
            Write-Host "Using default model gpt-5" -ForegroundColor Yellow
        }
    }
}

# Configuration
$CLEAN_MARKER = "[CLEAN]"
$PYTHON_SCRIPT = "tools\cleanup\single_file_cleaner.py"
$PROGRESS_LOG = "tmp\cleanup\progress.log"

# Colors for console output
$colors = @{
    Success = "Green"
    Warning = "Yellow"
    Error = "Red"
    Info = "Cyan"
    Progress = "Magenta"
}

# Initialize state
$script:totalFiles = 0
$script:processedFiles = 0
$script:cleanedFiles = 0
$script:skippedFiles = 0
$script:failedFiles = 0
$script:startTime = Get-Date

# State management
class ProcessingState {
    [hashtable]$ProcessedFiles = @{}
    [string[]]$FailedFiles = @()
    [string[]]$CleanedFiles = @()
    [string[]]$SkippedFiles = @()
    [datetime]$LastUpdate = (Get-Date)
}

function Write-ColoredOutput {
    param(
        [string]$Message,
        [string]$Color = "White",
        [switch]$NoNewline
    )
    
    # Handle color lookup with fallback
    $foregroundColor = if ($colors.ContainsKey($Color)) { $colors[$Color] } else { $Color }
    
    $params = @{
        ForegroundColor = $foregroundColor
    }
    if ($NoNewline) {
        $params.NoNewline = $true
    }
    
    Write-Host $Message @params
}

function Write-ProgressBar {
    param(
        [int]$Current,
        [int]$Total,
        [string]$Status = ""
    )
    
    if ($Total -eq 0) { return }
    
    $percentComplete = [math]::Round(($Current / $Total) * 100, 1)
    $barLength = 50
    $filledLength = [math]::Round(($percentComplete / 100) * $barLength)
    $bar = "#" * $filledLength + "-" * ($barLength - $filledLength)
    
    # Calculate ETA
    $elapsed = (Get-Date) - $script:startTime
    if ($Current -gt 0) {
        $avgTimePerFile = $elapsed.TotalSeconds / $Current
        $remainingFiles = $Total - $Current
        $eta = [TimeSpan]::FromSeconds($avgTimePerFile * $remainingFiles)
        $etaStr = "{0:hh\:mm\:ss}" -f $eta
    } else {
        $etaStr = "calculating..."
    }
    
    # Clear line and write progress
    Write-Host "`r" -NoNewline
    Write-Host "[" -NoNewline
    Write-Host $bar -ForegroundColor Green -NoNewline
    Write-Host "] " -NoNewline
    Write-Host "$percentComplete% " -ForegroundColor Yellow -NoNewline
    Write-Host "($Current/$Total) " -NoNewline
    Write-Host "ETA: $etaStr " -ForegroundColor Cyan -NoNewline
    
    if ($Status) {
        Write-Host "- $Status" -ForegroundColor Gray -NoNewline
    }
}

function Write-Summary {
    $elapsed = (Get-Date) - $script:startTime
    $elapsedStr = "{0:hh\:mm\:ss}" -f $elapsed
    
    Write-Host "`n`n" -NoNewline
    Write-ColoredOutput ("=" * 60) "Progress"
    Write-ColoredOutput "BATCH PROCESSING SUMMARY" "Progress"
    Write-ColoredOutput ("=" * 60) "Progress"
    
    Write-Host "Total Files:      " -NoNewline
    Write-ColoredOutput $script:totalFiles "Info"
    
    Write-Host "Already Clean:    " -NoNewline
    Write-ColoredOutput $script:skippedFiles "Info"
    
    Write-Host "Successfully Cleaned: " -NoNewline
    Write-ColoredOutput $script:cleanedFiles "Success"
    
    Write-Host "Failed:           " -NoNewline
    Write-ColoredOutput $script:failedFiles "Error"
    
    Write-Host "Time Elapsed:     " -NoNewline
    Write-ColoredOutput $elapsedStr "Info"
    
    if ($script:cleanedFiles -gt 0) {
        $avgTime = $elapsed.TotalSeconds / $script:cleanedFiles
        Write-Host "Avg Time/File:    " -NoNewline
        Write-ColoredOutput ("{0:F1} seconds" -f $avgTime) "Info"
    }
    
    Write-ColoredOutput ("=" * 60) "Progress"
}

function Load-State {
    param([string]$Path)
    
    if (Test-Path $Path) {
        try {
            $json = Get-Content $Path -Raw | ConvertFrom-Json
            $state = [ProcessingState]::new()
            
            # Convert JSON to hashtable for ProcessedFiles
            if ($json.ProcessedFiles) {
                $json.ProcessedFiles.PSObject.Properties | ForEach-Object {
                    $state.ProcessedFiles[$_.Name] = $_.Value
                }
            }
            
            $state.FailedFiles = @($json.FailedFiles)
            $state.CleanedFiles = @($json.CleanedFiles)
            $state.SkippedFiles = @($json.SkippedFiles)
            
            return $state
        } catch {
            Write-ColoredOutput "Warning: Could not load state file: $_" "Warning"
        }
    }
    
    return [ProcessingState]::new()
}

function Save-State {
    param(
        [ProcessingState]$State,
        [string]$Path
    )
    
    try {
        $State.LastUpdate = Get-Date
        
        # Ensure directory exists
        $dir = Split-Path $Path -Parent
        if (!(Test-Path $dir)) {
            New-Item -ItemType Directory -Path $dir -Force | Out-Null
        }
        
        $State | ConvertTo-Json -Depth 10 | Set-Content $Path -Encoding UTF8
    } catch {
        Write-ColoredOutput "Warning: Could not save state: $_" "Warning"
    }
}

function Test-FileAlreadyClean {
    param([string]$FilePath)
    
    try {
        $content = Get-Content $FilePath -Raw -ErrorAction Stop
        return $content.StartsWith($CLEAN_MARKER)
    } catch {
        return $false
    }
}

function Should-Retry {
    param([string]$ErrorMessage)
    if (-not $ErrorMessage) { return $false }
    $patterns = @(
        'timeout',            # generic timeouts
        'timed out',
        'connection.*(reset|refused|aborted|closed)',
        'temporary.*unavailable',
        'TLS handshake',
        'rate limit',
        '\b429\b',
        '\b502\b',
        '\b503\b',
        '\b504\b'
    )
    foreach ($p in $patterns) {
        if ($ErrorMessage -match $p) { return $true }
    }
    return $false
}

function Process-SingleFile {
    param(
        [string]$FilePath,
        [string]$ApiKey,
        [string]$BaseUrl,
        [string]$Model,
        [int]$MaxRetries
    )
    
    $fileName = Split-Path $FilePath -Leaf
    $success = $false
    $attempt = 0
    
    while ($attempt -lt $MaxRetries -and -not $success) {
        $attempt++
        
        if ($attempt -gt 1) {
            Write-Host "`n  " -NoNewline
            Write-ColoredOutput "Retry $attempt/$MaxRetries for $fileName" "Warning"
        }
        
        try {
            # Build command arguments
            $args = @(
                "run", "-e", "dev", "python", $PYTHON_SCRIPT,
                "--file", $FilePath,
                "--api-key", $ApiKey,
                "--model", $Model
            )
            
            if ($BaseUrl) {
                $args += "--base-url", $BaseUrl
            }
            
            # Execute Python script with timeout
            $processInfo = New-Object System.Diagnostics.ProcessStartInfo
            $processInfo.FileName = "pixi"
            $processInfo.Arguments = $args -join " "
            $processInfo.RedirectStandardOutput = $true
            $processInfo.RedirectStandardError = $true
            $processInfo.UseShellExecute = $false
            $processInfo.CreateNoWindow = $true
            
            $process = New-Object System.Diagnostics.Process
            $process.StartInfo = $processInfo
            
            # Start process
            $process.Start() | Out-Null
            
            # Wait with timeout (5 minutes per file)
            $timeout = 300000  # 5 minutes in milliseconds
            $completed = $process.WaitForExit($timeout)
            
            if (-not $completed) {
                # Timeout - kill the process
                $process.Kill()
                throw "Processing timeout after 5 minutes"
            }
            
            $exitCode = $process.ExitCode
            $output = $process.StandardOutput.ReadToEnd()
            $errorOutput = $process.StandardError.ReadToEnd()
            
            if ($exitCode -eq 0) {
                # Auto-add marker if model omitted it but content seems valid
                if (-not (Test-FileAlreadyClean -FilePath $FilePath)) {
                    try {
                        $raw = Get-Content $FilePath -Raw
                        if ($raw.Length -gt 0) {
                            "[CLEAN]\n$raw" | Set-Content $FilePath -Encoding UTF8
                        }
                    } catch { }
                }
                if (Test-FileAlreadyClean -FilePath $FilePath) {
                    $success = $true
                    return @{ Success = $true; Message = "Successfully cleaned" }
                }
                # If still not, treat as non-retriable content issue
                return @{ Success = $false; Message = "Missing marker after processing (no retry)" }
            } else {
                # Check for specific error patterns
                if ($errorOutput -match "Rate limit|429") {
                    Start-Sleep -Seconds 10
                    throw "rate limit"
                }
                if ($errorOutput -match "Connection timeout|Connection refused|Connection reset|timed out|502|503|504") {
                    throw "transient connection error"
                }
                # Non-transient -> break without further retries
                return @{ Success = $false; Message = "Exit code $exitCode (non-transient, no retry)" }
            }
            
        } catch {
            $errorMsg = $_.Exception.Message
            if (-not (Should-Retry -ErrorMessage $errorMsg)) {
                return @{ Success = $false; Message = "Non-retriable error: $errorMsg" }
            }
            if ($attempt -ge $MaxRetries) {
                return @{ Success = $false; Message = "Failed after $MaxRetries transient retries: $errorMsg" }
            }
            $waitTime = [math]::Min(3 * [math]::Pow(2, $attempt - 1), 45)
            Start-Sleep -Seconds $waitTime
        }
    }
    
    return @{ Success = $false; Message = "Failed to process file" }
}

function Main {
    Write-ColoredOutput ("=" * 60) "Progress"
    Write-ColoredOutput "CASCADEUR API DOCUMENTATION BATCH PROCESSOR" "Progress"
    Write-ColoredOutput ("=" * 60) "Progress"
    Write-Host ""
    
    # Display configuration
    Write-ColoredOutput "Configuration:" "Info"
    Write-Host "  Model:        $Model"
    Write-Host "  Base URL:     $BaseUrl"
    Write-Host "  Source:       $SourceDir"
    Write-Host "  Max Retries:  $MaxRetries"
    Write-Host ""
    
    # Load previous state
    $state = Load-State -Path $StateFile
    Write-ColoredOutput "Loading previous state..." "Info"
    
    # Get all markdown files
    $allFiles = Get-ChildItem -Path $SourceDir -Filter "*.md" -File | 
                Where-Object { $_.Name -notmatch "^(index|genindex|py-modindex|search)\.md$" }
    
    $script:totalFiles = $allFiles.Count
    Write-ColoredOutput "Found $($script:totalFiles) markdown files" "Info"
    Write-ColoredOutput "Retry policy: only transient connection/timeout/rate-limit errors will be retried." "Info"
    
    # Filter files to process
    $filesToProcess = @()
    
    foreach ($file in $allFiles) {
        $relativePath = $file.FullName.Replace((Get-Location).Path + "\", "")
        
        if (Test-FileAlreadyClean -FilePath $file.FullName) {
            $script:skippedFiles++
            if ($relativePath -notin $state.SkippedFiles) {
                $state.SkippedFiles += $relativePath
            }
        } elseif ($state.ProcessedFiles.ContainsKey($relativePath)) {
            # Already processed in this session
            $script:skippedFiles++
        } else {
            $filesToProcess += $file
        }
    }
    
    Write-ColoredOutput "Files to process: $($filesToProcess.Count)" "Info"
    Write-ColoredOutput "Already clean/processed: $script:skippedFiles" "Info"
    Write-Host ""
    
    # Check if single file cleaner exists, if not create it
    if (!(Test-Path $PYTHON_SCRIPT)) {
        Write-ColoredOutput "Creating single file cleaner script..." "Info"
        Create-SingleFileCleaner -Path $PYTHON_SCRIPT
    }
    
    # Process each file
    $fileNum = 0
    foreach ($file in $filesToProcess) {
        $fileNum++
        $fileName = $file.Name
        $relativePath = $file.FullName.Replace((Get-Location).Path + "\", "")
        
        # Update progress
        Write-ProgressBar -Current ($script:skippedFiles + $fileNum - 1) -Total $script:totalFiles -Status "Processing $fileName"
        
        # Process the file
        $result = Process-SingleFile -FilePath $file.FullName `
                                     -ApiKey $ApiKey `
                                     -BaseUrl $BaseUrl `
                                     -Model $Model `
                                     -MaxRetries $MaxRetries
        
        # Handle result
        if ($result.Success) {
            $script:cleanedFiles++
            $state.CleanedFiles += $relativePath
            $state.ProcessedFiles[$relativePath] = @{
                Status = "cleaned"
                Timestamp = (Get-Date).ToString("yyyy-MM-dd HH:mm:ss")
            }
            
            Write-Host "`r" -NoNewline
            Write-Host ("[{0}/{1}] " -f ($script:skippedFiles + $fileNum), $script:totalFiles) -NoNewline
            Write-ColoredOutput "[OK] $fileName" "Success"
        } else {
            $script:failedFiles++
            $state.FailedFiles += $relativePath
            $state.ProcessedFiles[$relativePath] = @{
                Status = "failed"
                Timestamp = (Get-Date).ToString("yyyy-MM-dd HH:mm:ss")
                Error = $result.Message
            }
            
            Write-Host "`r" -NoNewline
            Write-Host ("[{0}/{1}] " -f ($script:skippedFiles + $fileNum), $script:totalFiles) -NoNewline
            Write-ColoredOutput "[FAIL] $fileName - $($result.Message)" "Error"
            
            if (-not $ContinueOnError) {
                Write-ColoredOutput "`nStopping due to error (use -ContinueOnError to skip failed files)" "Error"
                break
            }
        }
        
        # Save state periodically (every 5 files)
        if ($fileNum % 5 -eq 0) {
            Save-State -State $state -Path $StateFile
        }
        
        # Update processed count
        $script:processedFiles = $script:skippedFiles + $fileNum
    }
    
    # Final state save
    Save-State -State $state -Path $StateFile
    
    # Show summary
    Write-Summary
    
    # Log completion
    $logEntry = @{
        Timestamp = (Get-Date).ToString("yyyy-MM-dd HH:mm:ss")
        TotalFiles = $script:totalFiles
        Cleaned = $script:cleanedFiles
        Failed = $script:failedFiles
        Skipped = $script:skippedFiles
        Duration = ((Get-Date) - $script:startTime).ToString()
    }
    
    # Ensure log directory exists
    $logDir = Split-Path $PROGRESS_LOG -Parent
    if (!(Test-Path $logDir)) {
        New-Item -ItemType Directory -Path $logDir -Force | Out-Null
    }
    
    # Append to log
    $logEntry | ConvertTo-Json -Compress | Add-Content $PROGRESS_LOG -Encoding UTF8
    
    # Return status
    if ($script:failedFiles -gt 0) {
        Write-ColoredOutput "`nNote: $script:failedFiles file(s) failed to process. Run again to retry." "Warning"
        exit 1
    } else {
        Write-ColoredOutput "`nAll files processed successfully!" "Success"
        exit 0
    }
}

function Create-SingleFileCleaner {
    param([string]$Path)
    
    $content = @'
#!/usr/bin/env python3
"""
Single file cleaner for use with PowerShell batch processor.
Cleans one markdown file at a time with LLM.
"""

import argparse
import asyncio
import sys
from pathlib import Path
from typing import Optional
import hashlib
from datetime import datetime

async def clean_single_file(
    file_path: Path,
    api_key: str,
    base_url: Optional[str] = None,
    model: str = 'gpt-5'
) -> bool:
    """Clean a single markdown file."""
    try:
        from litellm import acompletion
    except ImportError:
        print("Error: LiteLLM not installed", file=sys.stderr)
        return False
    
    # Read file
    try:
        content = file_path.read_text(encoding='utf-8', errors='ignore')
    except Exception as e:
        print(f"Error reading file: {e}", file=sys.stderr)
        return False
    
    # Check if already clean
    if content.startswith("[CLEAN]"):
        print(f"File already clean: {file_path}")
        return True
    
    # Build prompts
    system_prompt = """You are a precise documentation cleaning assistant for the Cascadeur Python API.
Transform the raw API documentation into a standardized, professional format.

STRICT RULES:
1. Preserve ALL factual API information exactly
2. Add [CLEAN] marker at the very beginning
3. Follow the standard structure (Overview, Class Definition, Methods, etc.)
4. Remove navigation menus and non-API content
5. Output ONLY valid Markdown"""
    
    user_prompt = f"""Clean this markdown documentation:

{content}

Remember to start with [CLEAN] marker."""
    
    # Determine model name for LiteLLM
    model_name = model
    if base_url and not base_url.startswith("https://api.openai.com"):
        if not model_name.startswith("openai/"):
            model_name = f"openai/{model_name}"
    
    # Use appropriate temperature for model
    temp = 1 if 'gpt-5' in model.lower() else 0.2
    
    try:
        # Make LLM call
        response = await acompletion(
            model=model_name,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            api_base=base_url,
            api_key=api_key,
            temperature=temp,
            max_tokens=8192,
            timeout=120,
        )
        
        cleaned = response['choices'][0]['message']['content'].strip()
        
        # Ensure [CLEAN] marker
        if not cleaned.startswith("[CLEAN]"):
            cleaned = f"[CLEAN]\n\n{cleaned}"
        
        # Add metadata comment
        original_hash = hashlib.md5(content.encode()).hexdigest()[:8]
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        cleaned = cleaned.replace(
            "[CLEAN]",
            f"[CLEAN]\n<!-- Cleaned by batch script {timestamp} | Original: {original_hash} -->"
        )
        
        # Write back to file
        file_path.write_text(cleaned, encoding='utf-8')
        print(f"Successfully cleaned: {file_path}")
        return True
        
    except Exception as e:
        print(f"Error cleaning file: {e}", file=sys.stderr)
        return False

async def main():
    parser = argparse.ArgumentParser(description='Clean a single markdown file')
    parser.add_argument('--file', required=True, type=Path, help='File to clean')
    parser.add_argument('--api-key', required=True, help='API key')
    parser.add_argument('--base-url', help='Base URL for LLM')
    parser.add_argument('--model', help='Model name (arg > env > default gpt-5)')
    
    args = parser.parse_args()
    
    # Hierarchical model resolution inside the embedded script
    resolved_model = args.model or os.getenv('CUSTOM_LLM_MODEL') or 'gpt-5'
    success = await clean_single_file(
        file_path=args.file,
        api_key=args.api_key,
        base_url=args.base_url,
        model=resolved_model
    )
    
    sys.exit(0 if success else 1)

if __name__ == '__main__':
    asyncio.run(main())
'@
    
    # Ensure directory exists
    $dir = Split-Path $Path -Parent
    if (!(Test-Path $dir)) {
        New-Item -ItemType Directory -Path $dir -Force | Out-Null
    }
    
    # Write file
    Set-Content -Path $Path -Value $content -Encoding UTF8
}

# Run main function
Main