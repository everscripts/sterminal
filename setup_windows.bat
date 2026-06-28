@echo off
REM Setup script for Windows
REM This script installs Python Terminal Emulator for Windows

setlocal enabledelayedexpansion

echo.
echo ========================================
echo Python Terminal for Windows - Setup
echo ========================================
echo.

REM Check if Python 3 is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python 3 is not installed or not in PATH.
    echo.
    echo Please install Python from: https://www.python.org/downloads/
    echo.
    echo During installation, make sure to:
    echo   1. Check "Add Python to PATH"
    echo   2. Choose "Install Now" or customize for all users
    echo.
    pause
    exit /b 1
)

REM Get Python version
for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo [OK] Python %PYTHON_VERSION% found

REM Create installation directory
set INSTALL_DIR=%APPDATA%\Python-Terminal
if not exist "%INSTALL_DIR%" (
    mkdir "%INSTALL_DIR%"
    echo [OK] Installation directory created: %INSTALL_DIR%
) else (
    echo [OK] Installation directory exists: %INSTALL_DIR%
)

REM Copy terminal file
echo.
echo Copying files...
copy /Y terminal_windows.py "%INSTALL_DIR%\terminal_windows.py" >nul 2>&1
if errorlevel 1 (
    echo Error: Failed to copy files
    pause
    exit /b 1
)
echo [OK] Files copied

REM Create batch file launcher
echo Creating launcher...
(
    echo @echo off
    echo python "%INSTALL_DIR%\terminal_windows.py" %%*
) > "%INSTALL_DIR%\py-terminal.bat"

REM Add to PATH via registry
setx PATH "%INSTALL_DIR%;!PATH!" >nul 2>&1

REM Create shortcut on Desktop (optional)
set DESKTOP=%USERPROFILE%\Desktop
if exist "%DESKTOP%" (
    (
        echo [InternetShortcut]
        echo URL=file:///%INSTALL_DIR%/py-terminal.bat
    ) > "%DESKTOP%\Python Terminal.lnk"
)

echo.
echo ========================================
echo [OK] Installation Complete!
echo ========================================
echo.
echo To start the terminal, run:
echo   py-terminal
echo or
echo   python "%INSTALL_DIR%\terminal_windows.py"
echo.
echo You may need to restart your terminal for PATH changes to take effect.
echo.
pause
