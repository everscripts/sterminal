#!/bin/bash
# Setup script for Linux Mint
# This script installs Python Terminal Emulator

set -e

echo "========================================"
echo "Python Terminal for Linux Mint - Setup"
echo "========================================"
echo ""

# Check if running on Linux
if [[ ! "$OSTYPE" == "linux-gnu"* ]]; then
    echo "❌ Error: This terminal is compatible only with Linux systems."
    exit 1
fi

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is not installed."
    echo "Install it with: sudo apt install python3 python3-pip"
    exit 1
fi

PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
echo "✓ Python $PYTHON_VERSION found"

# Create installation directory
INSTALL_DIR="$HOME/.local/share/python-terminal"
mkdir -p "$INSTALL_DIR"
echo "✓ Installation directory created: $INSTALL_DIR"

# Copy files
echo "Copying files..."
cp terminal.py "$INSTALL_DIR/"
cp terminal_gui.py "$INSTALL_DIR/"
chmod +x "$INSTALL_DIR/terminal.py" "$INSTALL_DIR/terminal_gui.py"
echo "✓ Files copied"

# Create symlinks in ~/.local/bin
mkdir -p "$HOME/.local/bin"
ln -sf "$INSTALL_DIR/terminal.py" "$HOME/.local/bin/py-terminal"
ln -sf "$INSTALL_DIR/terminal_gui.py" "$HOME/.local/bin/py-terminal-gui"
echo "✓ Symlinks created: ~/.local/bin/py-terminal and ~/.local/bin/py-terminal-gui"

# Add to PATH if necessary
if ! echo $PATH | grep -q "$HOME/.local/bin"; then
    echo "Adding ~/.local/bin to PATH..."
    echo 'export PATH="$HOME/.local/bin:$PATH"' >> "$HOME/.bashrc"
    echo "Please run: source ~/.bashrc"
fi

# Create desktop launcher
APPLICATIONS_DIR="$HOME/.local/share/applications"
mkdir -p "$APPLICATIONS_DIR"
DESKTOP_FILE="$APPLICATIONS_DIR/py-terminal-gui.desktop"
cat > "$DESKTOP_FILE" <<EOF
[Desktop Entry]
Name=STerminal GUI
GenericName=Python Terminal
Comment=Launch STerminal GUI
Exec=$HOME/.local/bin/py-terminal-gui
Icon=utilities-terminal
Terminal=false
Type=Application
Categories=Utility;Terminal;
StartupNotify=true
EOF
chmod 644 "$DESKTOP_FILE"
if command -v update-desktop-database &> /dev/null; then
    update-desktop-database "$APPLICATIONS_DIR" >/dev/null 2>&1 || true
fi

echo "✓ Desktop launcher created: $DESKTOP_FILE"

echo ""
echo "========================================"
echo "✓ Installation Complete!"
echo "========================================"
echo ""
echo "To start the terminal, run:"
echo "  py-terminal"
echo "  py-terminal-gui"
echo "or from the desktop menu, search for STerminal GUI."
echo ""
