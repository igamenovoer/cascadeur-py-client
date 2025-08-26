#!/usr/bin/env pwsh

<#
.SYNOPSIS
    Adds the Serena MCP server to Claude Code CLI in local scope

.DESCRIPTION
    This script adds the Serena MCP server configuration to Claude Code CLI
    using the claude mcp add-json command. The server will be added to the
    local scope.

.EXAMPLE
    .\add-serena-mcp.ps1
    Adds the Serena MCP server to the local configuration
#>

# Get the current directory and convert backslashes to forward slashes
$currentPath = (Get-Location).Path -replace '\\', '/'

# Get the serena.exe path dynamically and convert backslashes to forward slashes
try {
    $serenaPath = (Get-Command serena.exe -ErrorAction Stop).Source -replace '\\', '/'
    Write-Host "Found serena.exe at: $serenaPath" -ForegroundColor Green
} catch {
    Write-Host "❌ Error: serena.exe not found in PATH" -ForegroundColor Red
    Write-Host "Please make sure serena.exe is installed and available in your PATH." -ForegroundColor Yellow
    exit 1
}

# Define the MCP server configuration
$serverName = "serena-mcp"
$serverConfig = @{
    type = "stdio"
    command = $serenaPath
    args = @(
        "start-mcp-server",
        "--context",
        "ide-assistant",
        "--project",
        $currentPath
    )
    env = @{}
} | ConvertTo-Json -Compress

Write-Host "Adding Serena MCP server to Claude Code CLI..." -ForegroundColor Green
Write-Host "Server name: $serverName" -ForegroundColor Cyan
Write-Host "Serena path: $serenaPath" -ForegroundColor Cyan
Write-Host "Project path: $currentPath" -ForegroundColor Cyan
Write-Host "Configuration: $serverConfig" -ForegroundColor Cyan

# Check if the server already exists and remove it if it does
Write-Host "`nChecking if server already exists..." -ForegroundColor Yellow
claude mcp get $serverName 2>$null
if ($LASTEXITCODE -eq 0) {
    Write-Host "⚠️  Server '$serverName' already exists. Removing it first..." -ForegroundColor Yellow
    claude mcp remove $serverName
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✅ Successfully removed existing server." -ForegroundColor Green
    } else {
        Write-Host "❌ Failed to remove existing server." -ForegroundColor Red
    }
} else {
    Write-Host "✅ Server does not exist yet. Proceeding with addition." -ForegroundColor Green
}

try {
    # Add the MCP server to Claude Code CLI with local scope
    Write-Host "`nAdding MCP server..." -ForegroundColor Yellow
    $result = claude mcp add-json $serverName --scope local $serverConfig
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✅ Successfully added Serena MCP server to Claude Code!" -ForegroundColor Green
        
        # Verify the server was added
        Write-Host "`nVerifying server was added..." -ForegroundColor Yellow
        claude mcp list
        
        Write-Host "`nServer details:" -ForegroundColor Yellow
        claude mcp get $serverName
        
        Write-Host "`n📝 The server has been added to the local scope." -ForegroundColor Blue
        Write-Host "   This means it will be available in the local configuration." -ForegroundColor Blue
        Write-Host "   The configuration is stored in your local Claude Code settings." -ForegroundColor Blue
    } else {
        Write-Host "❌ Failed to add MCP server. Exit code: $LASTEXITCODE" -ForegroundColor Red
        Write-Host "Output: $result" -ForegroundColor Red
    }
} catch {
    Write-Host "❌ Error adding MCP server: $($_.Exception.Message)" -ForegroundColor Red
    Write-Host "Make sure Claude Code CLI is installed and accessible in your PATH." -ForegroundColor Yellow
    Write-Host "You can install it from: https://docs.anthropic.com/en/docs/claude-code" -ForegroundColor Yellow
}

Write-Host "`n🔧 Manual verification commands:" -ForegroundColor Magenta
Write-Host "   claude mcp list              # List all MCP servers" -ForegroundColor White
Write-Host "   claude mcp get serena-mcp    # Get server details" -ForegroundColor White
Write-Host "   claude mcp remove serena-mcp # Remove server if needed" -ForegroundColor White
