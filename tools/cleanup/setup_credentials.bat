@echo off
REM Secure setup script for API credentials
REM This helps configure API keys without exposing them in tracked files

echo ============================================
echo API Credentials Setup
echo ============================================
echo.
echo This script will help you securely configure your API credentials.
echo Your API key will NEVER be stored in tracked files.
echo.

:menu
echo Choose configuration method:
echo.
echo 1. Save to local untracked file (.api_key)
echo 2. Set as environment variable (current session)
echo 3. Set as environment variable (permanent for user)
echo 4. Display current configuration
echo 5. Exit
echo.
set /p choice="Enter your choice (1-5): "

if "%choice%"=="1" goto save_file
if "%choice%"=="2" goto set_temp_env
if "%choice%"=="3" goto set_perm_env
if "%choice%"=="4" goto show_config
if "%choice%"=="5" goto end

echo Invalid choice. Please try again.
goto menu

:save_file
echo.
set /p api_key="Enter your API key: "
echo %api_key% > .api_key
echo.
echo API key saved to .api_key (this file is gitignored)
echo.
set /p base_url="Enter base URL (press Enter for default https://yunwu.ai/v1): "
if not "%base_url%"=="" (
    echo BASE_URL=%base_url% >> .api_key
)
set /p model="Enter model name (press Enter for default gpt-5-2025-08-07): "
if not "%model%"=="" (
    echo MODEL=%model% >> .api_key
)
echo Configuration saved successfully!
echo.
pause
goto menu

:set_temp_env
echo.
set /p api_key="Enter your API key: "
set CUSTOM_LLM_API_KEY=%api_key%
echo.
set /p base_url="Enter base URL (press Enter for default): "
if not "%base_url%"=="" set CUSTOM_LLM_BASE_URL=%base_url%
set /p model="Enter model name (press Enter for default): "
if not "%model%"=="" set CUSTOM_LLM_MODEL=%model%
echo.
echo Environment variables set for current session.
echo.
pause
goto menu

:set_perm_env
echo.
echo This will set permanent environment variables for your user account.
echo.
set /p api_key="Enter your API key: "
setx CUSTOM_LLM_API_KEY "%api_key%"
echo.
set /p base_url="Enter base URL (press Enter to skip): "
if not "%base_url%"=="" setx CUSTOM_LLM_BASE_URL "%base_url%"
set /p model="Enter model name (press Enter to skip): "
if not "%model%"=="" setx CUSTOM_LLM_MODEL "%model%"
echo.
echo Permanent environment variables set.
echo Please restart your terminal for changes to take effect.
echo.
pause
goto menu

:show_config
echo.
echo Current Configuration:
echo ----------------------
if exist ".api_key" (
    echo Local file (.api_key): EXISTS
) else (
    echo Local file (.api_key): NOT FOUND
)
echo.
if "%CUSTOM_LLM_API_KEY%"=="" (
    echo Environment variable CUSTOM_LLM_API_KEY: NOT SET
) else (
    echo Environment variable CUSTOM_LLM_API_KEY: SET (hidden for security)
)
if not "%CUSTOM_LLM_BASE_URL%"=="" echo Environment variable CUSTOM_LLM_BASE_URL: %CUSTOM_LLM_BASE_URL%
if not "%CUSTOM_LLM_MODEL%"=="" echo Environment variable CUSTOM_LLM_MODEL: %CUSTOM_LLM_MODEL%
echo.
pause
goto menu

:end
echo.
echo Setup complete. You can now run the batch processing scripts.
echo.