@echo off
setlocal

set SCRIPT_DIR=%~dp0
set DIST_DIR=%SCRIPT_DIR%dist\windows
set RELEASE_DIR=%SCRIPT_DIR%dist\release\stterminal-windows-portable
set ZIP_PATH=%SCRIPT_DIR%dist\release\stterminal-windows-portable.zip

if not exist "%DIST_DIR%\stterminal.exe" if not exist "%DIST_DIR%\stterminal-gui.exe" (
    echo No built executables were found in dist\windows.
    echo Run package_windows.bat first, or place the .exe files there.
    exit /b 1
)

if exist "%RELEASE_DIR%" rmdir /s /q "%RELEASE_DIR%"
mkdir "%RELEASE_DIR%" >nul 2>&1

copy "%DIST_DIR%\stterminal.exe" "%RELEASE_DIR%\" >nul
copy "%DIST_DIR%\stterminal-gui.exe" "%RELEASE_DIR%\" >nul
copy "%SCRIPT_DIR%README_WINDOWS.md" "%RELEASE_DIR%\README.txt" >nul
copy "%SCRIPT_DIR%INSTALL_WINDOWS.md" "%RELEASE_DIR%\INSTALL.txt" >nul
copy "%SCRIPT_DIR%QUICKSTART_WINDOWS.md" "%RELEASE_DIR%\QUICKSTART.txt" >nul

if exist "%ZIP_PATH%" del /f /q "%ZIP_PATH%"
powershell -NoProfile -Command "Compress-Archive -Path '%RELEASE_DIR%\*' -DestinationPath '%ZIP_PATH%' -Force"

echo.
echo Release package created successfully.
echo ZIP file: %ZIP_PATH%
echo Folder: %RELEASE_DIR%
echo.
echo Upload the ZIP file to GitHub Releases, SourceForge, or another file host.
