@echo off
setlocal
cd /d "%~dp0"

if not exist ".venv\Scripts\python.exe" (
    call install_windows.bat
    if errorlevel 1 exit /b %errorlevel%
)

call ".venv\Scripts\python.exe" desktop.py
