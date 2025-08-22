@echo off
REM Batch script to run the documentation cleanup with pixi

echo ========================================
echo Cascadeur API Documentation Batch Cleaner
echo ========================================
echo.

REM Check if environment variables are set
if "%CUSTOM_LLM_API_KEY%"=="" (
    echo [INFO] CUSTOM_LLM_API_KEY not set, trying tools\cleanup\.api_key file...
    if exist tools\cleanup\.api_key (
        for /f "usebackq tokens=*" %%A in ("tools\cleanup\.api_key") do set CUSTOM_LLM_API_KEY=%%A
    )
)
if "%CUSTOM_LLM_API_KEY%"=="" (
    echo [ERROR] No API key. Set CUSTOM_LLM_API_KEY or create tools\cleanup\.api_key
    exit /b 1
)

REM Resolve Base URL: env > .api_base_url
set RESOLVED_BASE_URL=%CUSTOM_LLM_BASE_URL%
if "%RESOLVED_BASE_URL%"=="" (
    if exist tools\cleanup\.api_base_url (
        for /f "usebackq tokens=*" %%A in ("tools\cleanup\.api_base_url") do set RESOLVED_BASE_URL=%%A
    )
)

REM Resolve Model: env > .api_model_name > gpt-5
set RESOLVED_MODEL=%CUSTOM_LLM_MODEL%
if "%RESOLVED_MODEL%"=="" (
    if exist tools\cleanup\.api_model_name (
        for /f "usebackq tokens=*" %%A in ("tools\cleanup\.api_model_name") do set RESOLVED_MODEL=%%A
    ) else (
        set RESOLVED_MODEL=gpt-5
    )
)

echo Configuration:
echo   Model: %RESOLVED_MODEL%
echo   Base URL: %RESOLVED_BASE_URL%
echo.

REM Run the cleanup script with pixi
echo Starting cleanup process...
echo.
set CMD_ARGS=
if not "%RESOLVED_BASE_URL%"=="" set CMD_ARGS=--base-url "%RESOLVED_BASE_URL%"
pixi run -e dev python tools/cleanup/batch_clean_docs.py --api-key "%CUSTOM_LLM_API_KEY%" --model "%RESOLVED_MODEL%" %CMD_ARGS%

echo.
echo Cleanup process completed.
pause