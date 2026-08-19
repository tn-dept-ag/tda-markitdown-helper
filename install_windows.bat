@echo off
setlocal
cd /d "%~dp0"

where py >nul 2>nul
if errorlevel 1 (
    set "PYTHON_CMD=python"
) else (
    set "PYTHON_CMD=py -3"
)

if not exist ".venv\Scripts\python.exe" (
    %PYTHON_CMD% -m venv .venv
    if errorlevel 1 exit /b %errorlevel%
)

call ".venv\Scripts\python.exe" -m pip install --upgrade pip
if errorlevel 1 exit /b %errorlevel%

call ".venv\Scripts\python.exe" -m pip install -r requirements.txt
if errorlevel 1 exit /b %errorlevel%

echo.
echo Install complete.
echo Run launch.bat, run_desktop.bat, or run_web.bat next.
