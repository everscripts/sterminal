# Installation Guide for Linux Mint

## System Requirements

- **OS**: Linux Mint (Ubuntu-based systems also supported)
- **Python**: Python 3.6 or higher
- **Permissions**: User-level access (no root required for user installation)
- **Space**: ~100KB

## Prerequisites

### 1. Verify Python Installation

```bash
python3 --version
```

If Python 3 is not installed, install it:

```bash
sudo apt update
sudo apt install python3 python3-pip python3-dev
```

### 2. Verify Git (Optional)

For cloning the repository:

```bash
sudo apt install git
```

## Installation Methods

### Method 1: Automated Setup (Recommended)

The easiest way to install on Linux Mint.

#### Step 1: Download the Repository

```bash
# Clone the repository
git clone <repository-url> python-terminal
cd python-terminal/STerminal

# Or manually download and extract the files
# Make sure all files are in one directory
```

#### Step 2: Run the Setup Script

```bash
bash setup_linux_mint.sh
```

This script will:
- Verify Python 3 is installed
- Create installation directory at `~/.local/share/python-terminal/`
- Copy files and set executable permissions
- Create a symlink in `~/.local/bin/`
- Update your PATH (if necessary)

#### Step 3: Reload Shell Configuration

```bash
source ~/.bashrc
```

#### Step 4: Verify Installation

```bash
py-terminal --help
```

Or simply run:

```bash
py-terminal
```

---

### Method 2: Manual Installation

For advanced users or if the setup script fails.

#### Step 1: Create Installation Directory

```bash
mkdir -p ~/.local/share/python-terminal
cd ~/.local/share/python-terminal
```

#### Step 2: Copy Files

```bash
# Copy terminal.py from the source directory
cp /path/to/terminal.py ~/.local/share/python-terminal/

# Make it executable
chmod +x ~/.local/share/python-terminal/terminal.py
```

#### Step 3: Create Symlink

```bash
mkdir -p ~/.local/bin
ln -s ~/.local/share/python-terminal/terminal.py ~/.local/bin/py-terminal
```

#### Step 4: Add to PATH (if necessary)

Check if `~/.local/bin` is in your PATH:

```bash
echo $PATH | grep ".local/bin"
```

If not found, add it to `~/.bashrc`:

```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

---

### Method 3: System-Wide Installation (Requires Root)

For installing for all users on the system.

```bash
# Copy to system location
sudo cp terminal.py /usr/local/bin/py-terminal
sudo chmod +x /usr/local/bin/py-terminal

# Verify
py-terminal
```

---

## Uninstallation

### User Installation

```bash
# Remove symlink
rm ~/.local/bin/py-terminal

# Remove installation directory
rm -rf ~/.local/share/python-terminal/
```

### System-Wide Installation

```bash
sudo rm /usr/local/bin/py-terminal
```

---

## Post-Installation

### Create Desktop Shortcut (Optional)

Create a `.desktop` file for the application menu:

```bash
mkdir -p ~/.local/share/applications
cat > ~/.local/share/applications/py-terminal.desktop << EOF
[Desktop Entry]
Type=Application
Name=Python Terminal
Comment=Lightweight Python Terminal Emulator
Exec=py-terminal
Icon=utilities-terminal
Terminal=false
Categories=Utility;System;TerminalEmulator;
EOF
```

### Enable Application Menu Integration

```bash
update-desktop-database ~/.local/share/applications
```

---

## Troubleshooting

### Issue 1: Command Not Found

**Problem**: `py-terminal: command not found`

**Solution**:
```bash
# Verify Python installation
python3 --version

# Run with full path
python3 ~/.local/share/python-terminal/terminal.py

# Check PATH
echo $PATH

# Update PATH in ~/.bashrc
source ~/.bashrc
```

### Issue 2: Permission Denied

**Problem**: `Permission denied`

**Solution**:
```bash
# Make the script executable
chmod +x ~/.local/share/python-terminal/terminal.py
```

### Issue 3: Python Not Found

**Problem**: `python3: not found`

**Solution**:
```bash
# Install Python 3
sudo apt update
sudo apt install python3

# Verify installation
python3 --version
```

### Issue 4: Setup Script Fails

**Problem**: `setup_linux_mint.sh: command not found`

**Solution**:
```bash
# Make the script executable
chmod +x setup_linux_mint.sh

# Run with bash explicitly
bash setup_linux_mint.sh

# If still failing, use manual installation (Method 2)
```

### Issue 5: Import Error or Missing Modules

The terminal uses only Python standard library. If you encounter import errors:

```bash
# Reinstall Python
sudo apt install --reinstall python3

# Clear Python cache
find ~/.local/share/python-terminal -name "*.pyc" -delete
```

---

## Verification Checklist

After installation, verify everything is working:

```bash
# 1. Check Python version
python3 --version  # Should be 3.6 or higher

# 2. Check file permissions
ls -la ~/.local/bin/py-terminal  # Should show 'x' (executable)

# 3. Test direct execution
python3 ~/.local/share/python-terminal/terminal.py

# 4. Test symlink
which py-terminal

# 5. Run the terminal
py-terminal
```

---

## Advanced Configuration

### Creating Aliases

Add custom aliases to `~/.bashrc`:

```bash
alias pt='py-terminal'
alias pyterm='python3 ~/.local/share/python-terminal/terminal.py'
```

### Setting Default Shell

To use Python Terminal as your default shell (not recommended):

```bash
# Add to /etc/shells
sudo sh -c 'echo /usr/local/bin/py-terminal >> /etc/shells'

# Change your shell (use with caution)
chsh -s /usr/local/bin/py-terminal
```

---

## Environment Information

### Linux Mint Specific

This terminal is optimized for:
- **Linux Mint 21.x** (Ubuntu 22.04 LTS based)
- **Linux Mint 20.x** (Ubuntu 20.04 LTS based)
- **Linux Mint 19.x** (Ubuntu 18.04 LTS based)

Compatible with:
- Ubuntu 20.04, 22.04, 24.04
- Debian 10, 11, 12
- Other Debian-based systems

---

## Getting Help

For issues or questions:

1. Check the troubleshooting section above
2. Verify all prerequisites are met
3. Review the README.md for features and usage
4. Try manual installation (Method 2)

---

## Security Notes

- The terminal runs with your user privileges (no privilege escalation)
- All commands execute in your home directory or its subdirectories
- File operations are restricted to accessible locations
- System commands are available through the standard terminal

---

## Version Information

- **Application**: Python Terminal for Linux Mint
- **Version**: 1.0
- **Python**: 3.6+
- **Platform**: Linux Mint (Debian-based)
- **License**: Open Source

---

**Last Updated**: 2024
