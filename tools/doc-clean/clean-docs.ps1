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

  $message = "rewrite doc file $relPath"
  # IMPORTANT: Include the target markdown file itself so aider can read & edit it.
  $cmd = @('aider', $guideFull, $relPath, '--no-auto-commits', '--message', $message)
    if ($AiderExtraArgs) { $cmd += $AiderExtraArgs }

    $processInfo = New-Object System.Diagnostics.ProcessStartInfo
    $processInfo.FileName = $cmd[0]
    $processInfo.ArgumentList.AddRange($cmd[1..($cmd.Count-1)])
    $processInfo.RedirectStandardOutput = $true
    $processInfo.RedirectStandardError = $true
    $processInfo.UseShellExecute = $false

    $proc = [System.Diagnostics.Process]::Start($processInfo)
  $stdout = $proc.StandardOutput.ReadToEnd()
    $stderr = $proc.StandardError.ReadToEnd()
    $proc.WaitForExit()

    if ($proc.ExitCode -ne 0) {
      Write-Warning "aider exited with code $($proc.ExitCode) for $relPath"
      if ($stderr) { Write-Host $stderr -ForegroundColor Red }
      elseif ($stdout) { Write-Host $stdout -ForegroundColor DarkGray }
      continue
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
