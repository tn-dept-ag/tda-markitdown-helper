@echo off
setlocal
cd /d "%~dp0"

if not exist ".venv\Scripts\python.exe" (
    call install_windows.bat
    if errorlevel 1 exit /b %errorlevel%
)

:menu
cls
echo MarkItDown Helper
echo.
echo 1. Open desktop app
echo 2. Open Streamlit app
echo 3. Exit
echo.
set /p choice=Choose an option: 

if "%choice%"=="1" goto desktop
if "%choice%"=="2" goto web
if "%choice%"=="3" exit /b 0
goto menu

:desktop
call run_desktop.bat
exit /b %errorlevel%

:web
call run_web.bat
exit /b %errorlevel%

