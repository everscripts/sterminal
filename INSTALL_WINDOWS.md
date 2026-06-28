# Installation Guide for Windows

## System Requirements

- **OS**: Windows 7, 8, 10, 11, or Server editions
- **Python**: Python 3.6 or higher
- **Permissions**: User-level access (administrator not required)
- **Space**: ~200 KB
- **Terminal**: PowerShell, Command Prompt (cmd), or Windows Terminal

## Prerequisites

### 1. Verify or Install Python

#### Check if Python is Installed

Open **Command Prompt** or **PowerShell** and run:

```cmd
python --version
```

If you see a version (e.g., `Python 3.11.0`), Python is installed and ready.

#### If Python is Not Installed

1. Go to [python.org](https://www.python.org/downloads/)
2. Download **Python 3.11** or higher (latest recommended)
3. Run the installer
4. **IMPORTANT**: Check the box "Add Python to PATH"
5. Click "Install Now"
6. Verify installation:
   ```cmd
   python --version
   ```

---

## Installation Methods

### Method 1: Automated Setup (Recommended - Windows)

The easiest way to install on Windows.

#### Step 1: Download Files

Download all files from the repository or extract the ZIP file to a folder.

#### Step 2: Run Setup Script

1. Open **Command Prompt** as a normal user
2. Navigate to the folder containing the files:
   ```cmd
   cd C:\path\to\STerminal
   ```
3. Run the setup script:
   ```cmd
   setup_windows.bat
   ```

The script will:
- Verify Python 3 is installed
- Create installation directory at `%APPDATA%\Python-Terminal`
- Copy files
- Create launcher batch file
- Update your PATH environment variable
- Create desktop shortcut

#### Step 3: Restart Terminal

Close and reopen Command Prompt or PowerShell for PATH changes to take effect.

#### Step 4: Verify Installation

```cmd
py-terminal
```

If you see the terminal prompt, installation was successful!

---

### Method 2: Manual Installation

For advanced users or if the setup script fails.

#### Step 1: Create Installation Directory

```cmd
mkdir %APPDATA%\Python-Terminal
cd %APPDATA%\Python-Terminal
```

#### Step 2: Copy Files

Copy `terminal_windows.py` to the installation directory:

```cmd
copy C:\path\to\terminal_windows.py %APPDATA%\Python-Terminal\
```

#### Step 3: Create Launcher Batch File

Create a file named `py-terminal.bat` in `%APPDATA%\Python-Terminal\` with this content:

```batch
@echo off
python "%APPDATA%\Python-Terminal\terminal_windows.py" %*
```

#### Step 4: Add to PATH

**Option A: Using setx (Recommended)**

```cmd
setx PATH "%APPDATA%\Python-Terminal;%PATH%"
```

**Option B: Manual PATH Update**

1. Press `Win + X` → Select **System**
2. Click **Advanced system settings**
3. Click **Environment Variables**
4. Under "User variables", select **PATH** and click **Edit**
5. Click **New** and paste: `%APPDATA%\Python-Terminal`
6. Click **OK** three times

#### Step 5: Restart Terminal

Close and reopen Command Prompt or PowerShell.

#### Step 6: Verify

```cmd
py-terminal
```

---

### Method 3: System-Wide Installation (All Users)

For installing for all users on the computer (requires administrator access).

#### Step 1: Open Command Prompt as Administrator

1. Press `Win + R`
2. Type `cmd`
3. Press `Ctrl + Shift + Enter` (or right-click and select "Run as administrator")

#### Step 2: Create System Installation Directory

```cmd
mkdir "C:\Program Files\Python-Terminal"
copy terminal_windows.py "C:\Program Files\Python-Terminal\"
```

#### Step 3: Create Launcher

Create `py-terminal.bat` in `C:\Program Files\Python-Terminal\`:

```batch
@echo off
python "C:\Program Files\Python-Terminal\terminal_windows.py" %*
```

#### Step 4: Add to System PATH

```cmd
setx /M PATH "C:\Program Files\Python-Terminal;%PATH%"
```

#### Step 5: Restart and Test

```cmd
py-terminal
```

---

## Uninstallation

### User Installation

```cmd
REM Remove directory
rmdir /S /Q %APPDATA%\Python-Terminal

REM Remove PATH (manual edit of Environment Variables or use Command Prompt)
```

### System-Wide Installation

```cmd
REM Run as Administrator
rmdir /S /Q "C:\Program Files\Python-Terminal"
```

---

## Post-Installation

### Create Desktop Shortcut

Create a shortcut to quickly launch the terminal:

1. Right-click on Desktop → **New** → **Shortcut**
2. In the location field, enter:
   ```
   %APPDATA%\Python-Terminal\py-terminal.bat
   ```
3. Click **Next**
4. Name it: `Python Terminal`
5. Click **Finish**

### Add to Start Menu (Windows 10/11)

1. Create the desktop shortcut above
2. Copy the shortcut to:
   ```
   %APPDATA%\Microsoft\Windows\Start Menu\Programs
   ```
3. Now search for "Python Terminal" in the Start menu

### Windows Terminal Integration

If you use [Windows Terminal](https://microsoft.com/store/productId/9N0DX20HK701):

1. Open Windows Terminal settings (Ctrl + ,)
2. Add a new profile:
   ```json
   {
     "name": "Python Terminal",
     "commandline": "%APPDATA%\\Python-Terminal\\py-terminal.bat",
     "icon": "%SYSTEMROOT%\\System32\\cmd.exe",
     "startingDirectory": "%USERPROFILE%"
   }
   ```

---

## Troubleshooting

### Issue 1: "py-terminal: command not found" or "The system cannot find the file specified"

**Solution 1 - Check PATH**
```cmd
echo %PATH%
```

Make sure `%APPDATA%\Python-Terminal` is in the output.

**Solution 2 - Close and Reopen Terminal**
```cmd
REM Close Command Prompt/PowerShell completely
REM Open a new window
py-terminal
```

**Solution 3 - Run with Full Path**
```cmd
python "%APPDATA%\Python-Terminal\terminal_windows.py"
```

**Solution 4 - Update PATH**
```cmd
setx PATH "%APPDATA%\Python-Terminal;%PATH%"
REM Close and reopen Command Prompt
```

### Issue 2: "Python is not recognized as an internal or external command"

**Problem**: Python is not in PATH

**Solution**:
1. Verify Python is installed: `python --version`
2. If not found, install Python from [python.org](https://python.org)
3. **Check "Add Python to PATH" during installation**
4. Restart your terminal

### Issue 3: "Permission denied" or "Access denied"

**Problem**: File permissions issue

**Solution**:
```cmd
REM Run Command Prompt as Administrator
REM Then re-run setup
setup_windows.bat
```

### Issue 4: "ModuleNotFoundError" or "ImportError"

**Problem**: Python modules missing (shouldn't happen - terminal uses only standard library)

**Solution**:
```cmd
REM Reinstall Python
REM Use Control Panel → Programs → Uninstall a Program
REM Then reinstall from python.org
```

### Issue 5: Setup Script Fails

**Problem**: Error during `setup_windows.bat` execution

**Solution**:
1. Try running as Administrator
2. Use Manual Installation (Method 2)
3. Check if Python is in PATH: `python --version`

### Issue 6: Colors Not Working

**Problem**: ANSI color codes not displaying

**Solution**: Windows Terminal automatically detects ANSI support. If using older Command Prompt:
1. Update to Windows Terminal (recommended)
2. Or enable ANSI support via registry

---

## Verification Checklist

After installation, verify everything is working:

```cmd
REM 1. Check Python version
python --version
REM Expected: Python 3.6 or higher

REM 2. Check PATH includes Python-Terminal
echo %PATH%
REM Expected: %APPDATA%\Python-Terminal (or C:\Program Files\Python-Terminal)

REM 3. Check file exists
dir %APPDATA%\Python-Terminal\terminal_windows.py

REM 4. Test direct execution
python "%APPDATA%\Python-Terminal\terminal_windows.py"
REM Expected: Terminal prompt appears

REM 5. Test py-terminal command
py-terminal
REM Expected: Terminal prompt appears

REM 6. Test help
REM Inside terminal, type:
help
REM Expected: Command list displays
```

---

## Advanced Configuration

### Create Command Aliases

Add to your `doskey` configuration in Command Prompt:

```cmd
doskey pt=py-terminal
doskey pyterm=python "%APPDATA%\Python-Terminal\terminal_windows.py"
```

Or add to a batch file in your startup folder.

### PowerShell Profile

Add to your PowerShell profile (`$PROFILE`):

```powershell
Set-Alias -Name pt -Value py-terminal
function pyterm { python "$env:APPDATA\Python-Terminal\terminal_windows.py" }
```

### Run as Administrator (Windows Terminal)

If you need admin privileges for certain operations:

1. Right-click on `py-terminal.bat`
2. Select **Properties**
3. Go to **Advanced**
4. Check **Run as administrator**
5. Click **OK**

---

## Windows-Specific Features

The Windows version includes:

- **Windows Command Support**: Uses Windows commands (dir, type, etc.)
- **Path Compatibility**: Works with Windows backslash paths
- **Color Support**: ANSI colors in Windows Terminal and newer PowerShell
- **Process Management**: Windows-specific commands available
- **Registry Integration**: Updates PATH through registry
- **Batch Launcher**: Native batch file for easy execution

### Windows Commands You Can Use

```cmd
py-terminal
REM Inside terminal:

REM System Information
systeminfo
wmic os get name,version
tasklist

REM Network
ipconfig
nslookup google.com
ping google.com

REM Disk
dir C:\
diskpart
wmic logicaldisk get name

REM Processes
tasklist
taskkill /IM notepad.exe

REM Windows Management
wmic
wmis
```

---

## Performance

| Metric | Value |
|--------|-------|
| Startup Time (Cold) | 150-300 ms |
| Startup Time (Warm) | 100-150 ms |
| Memory Usage | 15-20 MB |
| Disk Space | ~200 KB |

---

## Security Notes

- Terminal runs with your user privileges
- No administrator access required for user installation
- File operations restricted to your user's accessible locations
- System commands execute with same privileges as your user account

---

## Environment Variables

Useful Windows environment variables for Python Terminal:

```
%APPDATA%      - User's app data folder
%USERPROFILE%  - User's home folder
%TEMP%         - Temporary files folder
%PATH%         - Search path for executables
%PATHEXT%      - Executable extensions (.COM, .EXE, .BAT, etc.)
%COMPUTERNAME% - Computer name
%USERNAME%     - Current user
```

---

## Additional Resources

- **Python Official**: https://python.org
- **Windows Terminal**: https://microsoft.com/store/productId/9N0DX20HK701
- **Windows CMD Reference**: https://docs.microsoft.com/windows-server/administration/windows-commands/windows-commands-ref
- **PowerShell Documentation**: https://docs.microsoft.com/powershell/

---

## FAQ

**Q: Can I run this on Windows Server?**  
A: Yes! Works on Windows Server 2016, 2019, 2022, etc.

**Q: Does it require administrator privileges?**  
A: No, user-level installation works fine. System-wide installation needs admin.

**Q: Is it compatible with PowerShell?**  
A: Yes! Works in Command Prompt, PowerShell, Windows Terminal, and Git Bash.

**Q: Can I integrate it with Windows Terminal?**  
A: Yes! See "Windows Terminal Integration" section above.

**Q: What about WSL (Windows Subsystem for Linux)?**  
A: WSL uses Linux, so use the Linux version (terminal.py). This version (terminal_windows.py) is for native Windows.

---

## Getting Help

1. Check the troubleshooting section above
2. Verify all prerequisites are met
3. Review the README_WINDOWS.md for features
4. Try manual installation if setup script fails

---

**Last Updated**: 2024  
**Version**: 1.0  
**Platform**: Windows 7, 8, 10, 11  
**Python**: 3.6+
