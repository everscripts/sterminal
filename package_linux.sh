#!/bin/bash
# Build Linux standalone executables with PyInstaller
# Requires PyInstaller installed in the active Python environment.

set -e

python3 -m PyInstaller --clean --onefile --distpath dist/linux --workpath build/linux --name stterminal terminal.py
python3 -m PyInstaller --clean --onefile --distpath dist/linux --workpath build/linux --name stterminal-gui terminal_gui.py

echo
echo "Build complete. Linux executables are available in dist/linux."
