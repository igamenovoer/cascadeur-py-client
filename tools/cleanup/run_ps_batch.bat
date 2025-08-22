@echo off
REM Convenient batch file to run PowerShell batch processor with credentials

echo ============================================
echo Cascadeur API Documentation Batch Processor
echo ============================================
echo.

REM Load credentials from environment or prompt user
REM NEVER hardcode API keys in tracked files!

REM Try to load from environment variables first
if "%CUSTOM_LLM_API_KEY%"=="" (
    echo [ERROR] CUSTOM_LLM_API_KEY environment variable not set!
    echo.
    echo Please set your API key using one of these methods:
    echo.
    echo Option 1: Set environment variable:
    echo   set CUSTOM_LLM_API_KEY=your-api-key-here
    echo.
    echo Option 2: Create untracked config file:
    echo   echo your-api-key-here > tools\cleanup\.api_key
    echo   Note: .api_key is gitignored
    echo.
    exit /b 1
)

set API_KEY=%CUSTOM_LLM_API_KEY%

REM Resolve Base URL: env > .api_base_url > empty(default provider base)
set BASE_URL=%CUSTOM_LLM_BASE_URL%
if "%BASE_URL%"=="" (
    if exist tools\cleanup\.api_base_url (
        for /f "usebackq tokens=*" %%A in ("tools\cleanup\.api_base_url") do set BASE_URL=%%A
    )
)

REM Resolve Model: env > .api_model_name > gpt-5
set MODEL=%CUSTOM_LLM_MODEL%
if "%MODEL%"=="" (
    if exist tools\cleanup\.api_model_name (
        for /f "usebackq tokens=*" %%A in ("tools\cleanup\.api_model_name") do set MODEL=%%A
    ) else (
        set MODEL=gpt-5
    )
)

echo Starting batch processing with:
echo   Model: %MODEL%
echo   Base URL: %BASE_URL%
echo.

REM Execute PowerShell script
powershell -ExecutionPolicy Bypass -File tools\cleanup\batch_process_docs.ps1 ^
    -ApiKey "%API_KEY%" ^
    -BaseUrl "%BASE_URL%" ^
    -Model "%MODEL%" ^
    -ContinueOnError

echo.
echo Batch processing completed.
pause