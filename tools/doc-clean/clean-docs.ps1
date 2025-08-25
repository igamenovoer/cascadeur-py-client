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
    $content = Get-Content -Path $_.FullName -First 5 -Raw
    # Normalize first non-empty line
    $firstLine = ($content -split "`n" | Where-Object { $_.Trim() -ne '' } | Select-Object -First 1)
    -not ($firstLine -match '^#?\s*\[CLEAN\]')
  }
}

$files = Get-UncleanMarkdownFiles -Dir $MarkdownDir
if ($Limit -gt 0) { $files = $files | Select-Object -First $Limit }

if (-not $files) {
  Write-Host 'No unclean markdown files found.' -ForegroundColor Green
  exit 0
}

Write-Host "Found $($files.Count) unclean markdown files." -ForegroundColor Cyan

# Core rewrite message template (single quoted to minimize escaping)
$messageTemplate = @'
Rewrite the target markdown API documentation file to the standardized format per the style guide already provided as an added file.
Rules:
- Remove any front matter (YAML or metadata), navigation menus, social/footer clutter, ads.
- Title: first line '# <FullyQualifiedName>' (use existing header text trimmed).
- Add Module/Source line if source_url was present: **Module:** `FullyQualifiedName`  **Source:** [Original Documentation Link](<source_url>)
- Sections (omit only if not applicable): Overview, Class Definition, Constructor, Methods, (optional Attributes if present), Usage Notes.
- For each method: heading ### `signature` followed by description (or 'Description not available in source.'), Parameters list, Returns, Example (if meaningful).
- Do NOT invent new methods; only use those clearly present.
- If descriptions missing, use the fallback phrase exactly once per item.
- Provide at least one minimal python example, valid syntax.
- Output ONLY the cleaned markdown content for the file.
'@

$guideFull = Resolve-Path -Path $GuidePath -ErrorAction Stop

$processed = 0
foreach ($file in $files) {
  $relPath = [IO.Path]::GetRelativePath((Resolve-Path .), $file.FullName)
  Write-Host "Cleaning: $relPath" -ForegroundColor Yellow

  if ($PSCmdlet.ShouldProcess($relPath, 'Rewrite with aider')) {
    # Run aider with guide file and target file
    $cmd = @(
      'aider',
      $guideFull,
      $relPath,
      '--no-auto-commits',
      '--message',
      $messageTemplate
    )
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
