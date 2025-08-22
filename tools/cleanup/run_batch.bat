@echo off
REM Simple batch processor launcher - uses .api_key file or environment variable

echo ============================================
echo Cascadeur API Documentation Batch Processor
echo ============================================
echo.

REM Run with default settings - API key will be loaded from .api_key file
echo Starting batch processing...
echo API key will be loaded from .api_key file or environment variable
echo.

powershell -ExecutionPolicy Bypass -File tools\cleanup\batch_process_docs.ps1 -ContinueOnError

echo.
echo Batch processing completed.
pause