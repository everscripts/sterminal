#!/usr/bin/env python3
"""
System configuration and management script for Python Terminal
Helps with testing, validation, and system-wide deployment
"""

import os
import sys
import platform
import subprocess
import shutil
from pathlib import Path


class SystemValidator:
    """Validates system compatibility and requirements"""
    
    @staticmethod
    def check_linux_mint():
        """Check if running on Linux Mint"""
        if sys.platform != 'linux':
            return False, f"System: {platform.system()}"
        
        try:
            with open('/etc/os-release', 'r') as f:
                os_info = f.read().lower()
                if 'mint' in os_info:
                    # Extract version
                    for line in os_info.split('\n'):
                        if 'version_id' in line:
                            version = line.split('=')[1].strip().strip('"')
                            return True, f"Linux Mint {version}"
        except FileNotFoundError:
            pass
        
        return False, "Could not verify Linux Mint"
    
    @staticmethod
    def check_python():
        """Check Python version"""
        version = sys.version_info
        if version.major == 3 and version.minor >= 6:
            return True, f"Python {version.major}.{version.minor}.{version.micro}"
        return False, f"Python {version.major}.{version.minor} (need 3.6+)"
    
    @staticmethod
    def check_permissions():
        """Check user permissions"""
        home = os.path.expanduser('~')
        local_bin = os.path.join(home, '.local', 'bin')
        
        # Check if directory exists or can be created
        try:
            os.makedirs(local_bin, exist_ok=True)
            return True, "User installation available"
        except PermissionError:
            return False, "No permission to create ~/.local/bin"


class InstallationManager:
    """Manages installation and deployment"""
    
    @staticmethod
    def install_user():
        """Install for current user"""
        print("Installing for current user...")
        
        home = os.path.expanduser('~')
        install_dir = os.path.join(home, '.local', 'share', 'python-terminal')
        bin_dir = os.path.join(home, '.local', 'bin')
        
        # Create directories
        Path(install_dir).mkdir(parents=True, exist_ok=True)
        Path(bin_dir).mkdir(parents=True, exist_ok=True)
        
        # Copy terminal.py
        source = 'terminal.py'
        if os.path.exists(source):
            shutil.copy2(source, os.path.join(install_dir, 'terminal.py'))
            os.chmod(os.path.join(install_dir, 'terminal.py'), 0o755)
        
        # Create symlink
        symlink_path = os.path.join(bin_dir, 'py-terminal')
        if os.path.exists(symlink_path):
            os.remove(symlink_path)
        
        os.symlink(
            os.path.join(install_dir, 'terminal.py'),
            symlink_path
        )
        
        print(f"✓ Installed to {install_dir}")
        print(f"✓ Symlink created at {symlink_path}")
    
    @staticmethod
    def verify_installation():
        """Verify installation is working"""
        print("\nVerifying installation...")
        
        try:
            result = subprocess.run(
                ['python3', 'terminal.py', '-c'],
                capture_output=True,
                timeout=2
            )
            print("✓ Terminal script is executable")
        except Exception as e:
            print(f"✗ Error: {e}")


def print_header(title):
    """Print formatted header"""
    print("\n" + "=" * 50)
    print(f"  {title}")
    print("=" * 50)


def main():
    """Main validation and setup function"""
    print_header("Python Terminal System Validator")
    
    # Check system requirements
    print("\nSystem Requirements Check:")
    print("-" * 50)
    
    # Linux Mint check
    is_mint, mint_info = SystemValidator.check_linux_mint()
    status = "✓" if is_mint else "✗"
    print(f"{status} Linux Mint: {mint_info}")
    
    # Python check
    is_python_ok, python_info = SystemValidator.check_python()
    status = "✓" if is_python_ok else "✗"
    print(f"{status} Python: {python_info}")
    
    # Permissions check
    has_perms, perms_info = SystemValidator.check_permissions()
    status = "✓" if has_perms else "✗"
    print(f"{status} Permissions: {perms_info}")
    
    # Summary
    print("\n" + "-" * 50)
    if is_python_ok and has_perms:
        print("✓ System is compatible with Python Terminal")
        
        if is_mint:
            print("✓ Optimized for Linux Mint")
        else:
            print("⚠ Linux distribution detection failed")
            print("  Terminal should still work on Debian-based systems")
    else:
        print("✗ System requirements not met")
        return 1
    
    # Installation info
    print_header("Installation Information")
    print("""
For installation, run one of:

1. Automated Setup (Recommended):
   bash setup_linux_mint.sh

2. Manual Installation:
   - See INSTALL_LINUX_MINT.md for detailed steps

3. System-Wide Installation (requires sudo):
   sudo cp terminal.py /usr/local/bin/py-terminal
   sudo chmod +x /usr/local/bin/py-terminal
    """)
    
    # File structure
    print_header("File Structure")
    required_files = {
        'terminal.py': 'Main terminal application',
        'setup_linux_mint.sh': 'Installation script',
        'README.md': 'User documentation',
        'INSTALL_LINUX_MINT.md': 'Installation guide',
        'requirements.txt': 'Dependencies',
    }
    
    all_present = True
    for filename, description in required_files.items():
        exists = "✓" if os.path.exists(filename) else "✗"
        print(f"{exists} {filename:<25} - {description}")
        if not os.path.exists(filename):
            all_present = False
    
    if not all_present:
        print("\n⚠ Some files are missing. Ensure all files are in the same directory.")
    else:
        print("\n✓ All required files present")
    
    # Quick start
    print_header("Quick Start")
    print("""
After installation:

1. Reload shell configuration:
   source ~/.bashrc

2. Start the terminal:
   py-terminal

3. View available commands:
   help

4. Exit the terminal:
   exit
    """)
    
    print("=" * 50)
    return 0


if __name__ == '__main__':
    sys.exit(main())
