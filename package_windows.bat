@echo off
REM Build Windows standalone executables with PyInstaller
REM Requires PyInstaller installed in the active Python environment.

python -m PyInstaller --clean --onefile --distpath dist/windows --workpath build/windows --name stterminal terminal_windows.py
python -m PyInstaller --clean --onefile --windowed --distpath dist/windows --workpath build/windows --name stterminal-gui terminal_gui.py

echo.
echo Build complete.
echo Windows executables are available in dist\windows.
