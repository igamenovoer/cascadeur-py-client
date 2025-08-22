@echo off
REM Advanced batch file to run PowerShell batch processor with configurable parameters

echo ============================================
echo Cascadeur API Documentation Batch Processor
echo ============================================
echo.

REM Configuration - Load from environment or config file
REM NEVER hardcode API keys in tracked files!

REM Check for API key in environment or config file
if "%CUSTOM_LLM_API_KEY%"=="" (
    REM Try to load from untracked config file
    if exist "tools\cleanup\.api_key" (
        set /p API_KEY=<tools\cleanup\.api_key
    ) else (
        echo [ERROR] No API key found!
        echo.
        echo Please provide your API key using one of these methods:
        echo.
        echo Option 1: Set environment variable:
        echo   set CUSTOM_LLM_API_KEY=your-api-key-here
        echo.
        echo Option 2: Create untracked config file:
        echo   echo your-api-key-here ^> tools\cleanup\.api_key
        echo.
        echo Option 3: Pass as third argument:
        echo   %0 5 gpt-5-2025-08-07 your-api-key-here
        echo.
        exit /b 1
    )
) else (
    set API_KEY=%CUSTOM_LLM_API_KEY%
)

REM Load other settings with defaults
set BASE_URL=%CUSTOM_LLM_BASE_URL%
if "%BASE_URL%"=="" (
    if exist "tools\cleanup\.api_base_url" (
         set /p BASE_URL=<tools\cleanup\.api_base_url
    )
)
if "%BASE_URL%"=="" (
    echo [ERROR] No Base URL found. Provide via CUSTOM_LLM_BASE_URL env or tools\cleanup\.api_base_url or pass as -BaseUrl in PowerShell.
    goto :EOF
)
set MODEL=%CUSTOM_LLM_MODEL%
if "%MODEL%"=="" (
    if exist "tools\cleanup\.api_model_name" (
         set /p MODEL=<tools\cleanup\.api_model_name
    )
)
if "%MODEL%"=="" set MODEL=gpt-5
set MAX_RETRIES=5
set SOURCE_DIR=casey-docs\markdown
set STATE_FILE=tmp\cleanup\ps_batch_state.json

REM Parse command line arguments if provided
if not "%1"=="" set MAX_RETRIES=%1
if not "%2"=="" set MODEL=%2
if not "%3"=="" set API_KEY=%3

echo Configuration:
echo   Model:        %MODEL%
echo   Base URL:     %BASE_URL%
echo   Max Retries:  %MAX_RETRIES%
echo   Source Dir:   %SOURCE_DIR%
echo   State File:   %STATE_FILE%
echo.
echo Usage: %0 [max_retries] [model] [api_key]
echo   Example: %0 5 gpt-5-2025-08-07
echo   Example: %0 10 (for 10 retries with default model)
echo.
echo Starting batch processing...
echo Press Ctrl+C to stop (progress will be saved)
echo.

REM Execute PowerShell script with all parameters
REM If API_KEY is set from env/config, use it; otherwise script will use .api_key file
if "%API_KEY%"=="" (
    REM Let the PowerShell script handle loading from .api_key
    powershell -ExecutionPolicy Bypass -File tools\cleanup\batch_process_docs.ps1 ^
        -BaseUrl "%BASE_URL%" ^
        -Model "%MODEL%" ^
        -MaxRetries %MAX_RETRIES% ^
        -SourceDir "%SOURCE_DIR%" ^
        -StateFile "%STATE_FILE%" ^
        -ContinueOnError
) else (
    powershell -ExecutionPolicy Bypass -File tools\cleanup\batch_process_docs.ps1 ^
        -ApiKey "%API_KEY%" ^
        -BaseUrl "%BASE_URL%" ^
        -Model "%MODEL%" ^
        -MaxRetries %MAX_RETRIES% ^
        -SourceDir "%SOURCE_DIR%" ^
        -StateFile "%STATE_FILE%" ^
        -ContinueOnError
)

echo.
echo Batch processing completed.

REM Check if we should show failed files
if exist "%STATE_FILE%" (
    echo.
    echo Checking for failed files...
    powershell -Command "& { $state = Get-Content '%STATE_FILE%' | ConvertFrom-Json; if ($state.FailedFiles.Count -gt 0) { Write-Host 'Failed files:' -ForegroundColor Red; $state.FailedFiles | ForEach-Object { Write-Host \"  - $_\" -ForegroundColor Yellow } } else { Write-Host 'All files processed successfully!' -ForegroundColor Green } }"
)

pause