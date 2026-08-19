@echo off
setlocal
cd /d "%~dp0"

if not exist ".venv\Scripts\python.exe" (
    call install_windows.bat
    if errorlevel 1 exit /b %errorlevel%
)

call ".venv\Scripts\python.exe" -m pip install pyinstaller
if errorlevel 1 exit /b %errorlevel%

call ".venv\Scripts\pyinstaller.exe" --noconfirm --clean --onefile --windowed --name MarkItDownHelper --collect-data magika desktop.py
if errorlevel 1 exit /b %errorlevel%

echo.
echo Build complete.
echo Output: dist\MarkItDownHelper.exe
