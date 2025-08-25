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
  [switch]$TagClean,  # Deprecated: tagging now always applied; retained for backward compat
  [string]$GuidePath = 'context/hints/howto-clean-api-documentation.md',
  [string]$MarkdownDir = 'casey-docs/markdown',
  [string]$AiderExtraArgs = ''
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Get-UncleanMarkdownFiles {
  param([string]$Dir)
  Get-ChildItem -Path $Dir -Filter *.md -File -Recurse | Where-Object {
    $lines = Get-Content -Path $_.FullName -TotalCount 8
    $firstLine = ($lines | Where-Object { $_.Trim() -ne '' } | Select-Object -First 1).Trim()
    # Clean if first non-empty line is exactly [CLEAN]
    -not ($firstLine -eq '[CLEAN]')
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

Standardize per project rules:
1. If a YAML front matter block (--- ... ---) exists at top, remove it entirely.
2. Ensure the FIRST non-empty line is exactly: [CLEAN]
3. After a blank line, provide a single H1 title: # $($file.BaseName)
4. Add an '## Overview' section with 2-4 concise sentences describing purpose & context.
5. Include '## Class Definition' (or '## Function Definition') with a python code fence of the signature(s).
6. Sections order (omit if not applicable): Constructor, Methods, Attributes, Usage Notes.
7. For each method: heading '### `signature`', one-sentence summary, Parameters bullet list (name: type – description), Returns line, Notes (optional).
8. Do NOT fabricate undocumented params, types, or behavior. If unknown, say 'undocumented' minimally or omit.
9. No duplicate info; keep formatting tight; use ```python fences for code.
10. Do not prepend [CLEAN] to the title; the tag must stand alone as its own line.
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
    # Always enforce single-line [CLEAN] tag at top
    $content = Get-Content -Path $file.FullName -Raw
    $lines = [System.Collections.Generic.List[string]]::new()
    $content -split "`n" | ForEach-Object { $lines.Add($_) }

    # Remove any legacy '# [CLEAN] ...' header variants
    if ($lines.Count -gt 0 -and $lines[0] -match '^#\s*\[CLEAN\]') { $lines.RemoveAt(0) }

    # Strip leading blank lines
    while ($lines.Count -gt 0 -and $lines[0].Trim() -eq '') { $lines.RemoveAt(0) }

    # Insert [CLEAN] tag if missing
    if (-not ($lines.Count -gt 0 -and $lines[0].Trim() -eq '[CLEAN]')) {
      $lines.Insert(0, '[CLEAN]')
      $lines.Insert(1, '')
    }

    $newContent = ($lines -join "`n").TrimEnd() + "`n"
    if ($newContent -ne $content) {
      Set-Content -Path $file.FullName -Value $newContent -Encoding UTF8
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
