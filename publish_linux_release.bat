@echo off
setlocal

set SCRIPT_DIR=%~dp0
set RELEASE_DIR=%SCRIPT_DIR%dist\release\stterminal-linux-portable
set TAR_PATH=%SCRIPT_DIR%dist\release\stterminal-linux-portable.tar.gz

if exist "%RELEASE_DIR%" rmdir /s /q "%RELEASE_DIR%"
mkdir "%RELEASE_DIR%" >nul 2>&1

if exist "%SCRIPT_DIR%dist\linux\stterminal" copy "%SCRIPT_DIR%dist\linux\stterminal" "%RELEASE_DIR%\" >nul
if exist "%SCRIPT_DIR%dist\linux\stterminal-gui" copy "%SCRIPT_DIR%dist\linux\stterminal-gui" "%RELEASE_DIR%\" >nul

copy "%SCRIPT_DIR%README.md" "%RELEASE_DIR%\README.txt" >nul
copy "%SCRIPT_DIR%INSTALL_LINUX_MINT.md" "%RELEASE_DIR%\INSTALL.txt" >nul
copy "%SCRIPT_DIR%QUICKSTART.md" "%RELEASE_DIR%\QUICKSTART.txt" >nul

if exist "%TAR_PATH%" del /f /q "%TAR_PATH%"

powershell -NoProfile -Command "$source = '%RELEASE_DIR%'; $dest = '%TAR_PATH%'; if (Test-Path $dest) { Remove-Item $dest -Force }; $files = Get-ChildItem $source -Force; $temp = Join-Path $env:TEMP 'stterminal-linux-portable'; if (Test-Path $temp) { Remove-Item $temp -Recurse -Force }; New-Item -ItemType Directory -Path $temp -Force | Out-Null; Copy-Item ($source + '\*') $temp -Recurse -Force; tar -czf $dest -C $temp ." 

echo Portable Linux release created successfully.
echo Archive: %TAR_PATH%
echo Folder: %RELEASE_DIR%
