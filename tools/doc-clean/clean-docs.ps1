<#
Batch clean documentation markdown files under casey-docs/markdown using aider.

Strategy:
- Identify all *.md files in casey-docs/markdown that do NOT begin with "# [CLEAN]" or "[CLEAN]" on the first non-empty line.
- For each file, run aider with the style guide file as a reference context and a --message instructing rewrite.
- Avoid re-processing already cleaned files (prefixed with [CLEAN]).
- Append a banner "[CLEAN]" to the first header line after successful rewrite (optional toggle via -TagClean switch).

Requirements:
- Assumes `aider` is on PATH and system prompt config already in .aider.conf.yml (or style file passed each run).
- Uses context/hints/howto-clean-api-documentation.md as the guide file to add as a chat file.
- Runs sequentially; can add -WhatIf to preview.
- Supports -Limit to process only N files.

Usage examples:
  pwsh ./tools/doc-clean/clean-docs.ps1
  pwsh ./tools/doc-clean/clean-docs.ps1 -Limit 10 -Verbose
  pwsh ./tools/doc-clean/clean-docs.ps1 -TagClean:$false

#>
[CmdletBinding(SupportsShouldProcess=$true)]
param(
  [int]$Limit = 0,
  [switch]$TagClean,
  [string]$GuidePath = 'context/hints/howto-clean-api-documentation.md',
  [string]$MarkdownDir = 'casey-docs/markdown',
  [string]$AiderExtraArgs = ''
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Get-UncleanMarkdownFiles {
  param([string]$Dir)
  Get-ChildItem -Path $Dir -Filter *.md -File -Recurse | Where-Object {
    # Read only first few lines (can't mix -Raw with -TotalCount)
    $lines = Get-Content -Path $_.FullName -TotalCount 8
    $firstLine = $lines | Where-Object { $_.Trim() -ne '' } | Select-Object -First 1
    -not ($firstLine -and ($firstLine -match '^#?\s*\[CLEAN\]'))
  }
}

$files = @(Get-UncleanMarkdownFiles -Dir $MarkdownDir)
if ($Limit -gt 0) { $files = @($files | Select-Object -First $Limit) }

if (-not $files -or $files.Count -eq 0) {
  Write-Host 'No unclean markdown files found.' -ForegroundColor Green
  exit 0
}

Write-Host ("Found {0} unclean markdown file{1}." -f $files.Count, $(if ($files.Count -eq 1) { '' } else { 's' })) -ForegroundColor Cyan

# Per-file instruction will be a concise message: "rewrite doc file <relative path>"

$guideFull = Resolve-Path -Path $GuidePath -ErrorAction Stop

$processed = 0
foreach ($file in $files) {
  $relPath = [IO.Path]::GetRelativePath((Resolve-Path .), $file.FullName)
  Write-Host "Cleaning: $relPath" -ForegroundColor Yellow

  if ($PSCmdlet.ShouldProcess($relPath, 'Rewrite with aider')) {
    # Run aider with guide file and target file
  # Capture pre-change hash to detect no-op rewrites
  $preHash = (Get-FileHash -Algorithm SHA256 -Path $file.FullName).Hash

  $message = @"
rewrite doc file $relPath

Transform it to the standardized API doc structure:
1. Remove the YAML front matter block delimited by --- at the top.
2. Start with: # [CLEAN] $($file.BaseName)
3. Add an Overview section summarizing purpose in 2-4 concise sentences.
4. Provide a Class Definition code block if it's a class; else a Function Definition block.
5. List Constructor (if class) and then Methods, each with: signature (backticks), brief description, parameter bullets (name: type – description), return type, and important notes. Skip duplicates.
6. Add Attributes section if there are notable attributes; otherwise omit.
7. End with a Usage Notes section containing any caveats or typical usage patterns.
8. No trailing blank heading, keep formatting tight, wrap code fences with ```python where relevant.
9. Avoid repeating the module path in every heading; concise names only after the main title.
10. Do not fabricate APIs; only include what is evidently present.
"@
  # Use a temporary message file to avoid CLI arg parsing issues with spaces.
  $msgFile = New-TemporaryFile
  Set-Content -Path $msgFile -Value $message -Encoding UTF8
  # Include the target markdown file so aider can read & edit it.
  $cmd = @('aider', $guideFull, $relPath, '--message-file', $msgFile, '--no-auto-commits')
    if ($AiderExtraArgs) { $cmd += $AiderExtraArgs }

    $outFile = New-TemporaryFile
    $errFile = New-TemporaryFile
    try {
      $argList = $cmd[1..($cmd.Count-1)]
      $proc = Start-Process -FilePath $cmd[0] -ArgumentList $argList -NoNewWindow -Wait -PassThru -RedirectStandardOutput $outFile -RedirectStandardError $errFile
      $stdout = if (Test-Path $outFile) { Get-Content -Path $outFile -Raw } else { '' }
      $stderr = if (Test-Path $errFile) { Get-Content -Path $errFile -Raw } else { '' }
      if ($proc.ExitCode -ne 0) {
        Write-Warning "aider exited with code $($proc.ExitCode) for $relPath"
        if ($stderr) { Write-Host $stderr -ForegroundColor Red }
        elseif ($stdout) { Write-Host $stdout -ForegroundColor DarkGray }
        continue
      }
    }
    finally {
      if (Test-Path $outFile) { Remove-Item $outFile -Force }
      if (Test-Path $errFile) { Remove-Item $errFile -Force }
    }

    # Tag cleaned file if requested
    if ($TagClean) {
      $content = Get-Content -Path $file.FullName -Raw
      if ($content -notmatch '^# \[CLEAN\] ') {
        $content = $content -replace '^#\s+', '# [CLEAN] '  # prefix first header
        Set-Content -Path $file.FullName -Value $content -Encoding UTF8
      }
    }

    # Recompute hash; skip staging if unchanged
    $postHash = (Get-FileHash -Algorithm SHA256 -Path $file.FullName).Hash
    if ($preHash -eq $postHash) {
      Write-Warning "No changes detected for $relPath (skipping add). Consider enriching the rewrite message if this persists."
      continue
    }

    git add -- "$relPath" 2>$null
    $processed++
  }
}

if ($processed -gt 0) {
  git commit -m "docs: batch clean $processed markdown API docs" | Out-Null
  Write-Host "Committed $processed cleaned docs." -ForegroundColor Green
} else {
  Write-Host 'No files were processed.' -ForegroundColor Yellow
}
