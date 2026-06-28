# Quick Start Guide - Python Terminal for Windows

> **Get up and running in less than 5 minutes!**

---

## 60-Second Installation

### Step 1: Download
```cmd
REM Navigate to the folder with the files
cd C:\path\to\STerminal
```

### Step 2: Install
```cmd
setup_windows.bat
```

### Step 3: Start
```cmd
REM Close and reopen Command Prompt or PowerShell
py-terminal
```

**Done!** You now have a working Python Terminal for Windows. 🎉

---

## Essential Commands

### Create and Navigate

```cmd
REM Inside py-terminal

REM Create folders
mkdir projects
cd projects

REM Create files
touch README.md
touch script.py

REM List contents
ls
REM or Windows-style
dir

REM Go back
cd ..
```

### View and Edit Files

```cmd
REM Display file contents
cat README.md
REM or Windows-style
type README.md

REM Show file info
dir script.py
```

### Copy and Move

```cmd
REM Copy file
cp README.md README.backup

REM Move file
mv script.py scripts\

REM Remove file
rm README.backup

REM Remove folder
rmdir old_folder
```

### Get Help

```cmd
REM Show all commands
help

REM Show command history
history

REM Exit terminal
exit
```

---

## Common Use Cases

### Scenario 1: Organize Project Files

```cmd
py-terminal
mkdir my_project
cd my_project
mkdir src
mkdir tests
mkdir docs
touch src\main.py
touch tests\test.py
touch README.md
ls
exit
```

### Scenario 2: Backup Files

```cmd
py-terminal
cp important_file.txt important_file.txt.backup
cp important_file.txt.backup C:\Backups\
history
exit
```

### Scenario 3: Run Python Scripts

```cmd
py-terminal
python my_script.py
python my_script.py --arg1 value1
pip install requests
exit
```

### Scenario 4: Use Git

```cmd
py-terminal
git status
git add .
git commit -m "Initial commit"
git push origin main
exit
```

### Scenario 5: System Information

```cmd
py-terminal
systeminfo
tasklist
ipconfig
exit
```

---

## Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl+C` | Cancel current command |
| `Ctrl+Z` then `Enter` | Exit terminal (alternative) |
| `↑` / `↓` | Navigate command history |
| `Tab` | Command autocomplete (in some terminals) |
| `Ctrl+L` | Clear screen (in some terminals) |

---

## Quick Commands Reference

### File Operations
```cmd
mkdir folder              # Create folder
touch file.txt           # Create file
cp file.txt file2.txt    # Copy file
mv file.txt backup\      # Move file
rm file.txt              # Delete file
rmdir folder             # Delete folder
rm -r folder             # Delete folder with contents
```

### Navigation
```cmd
cd folder                # Go into folder
cd ..                    # Go up one level
cd C:\                   # Go to root
pwd                      # Show current folder
ls                       # List files
dir                      # List files (Windows style)
```

### View Contents
```cmd
cat file.txt             # View file
type file.txt            # View file (Windows)
```

### Help & Exit
```cmd
help                     # Show all commands
history                  # Show command history
clear                    # Clear screen
cls                      # Clear screen (Windows)
exit                     # Exit terminal
```

---

## Useful Aliases

The terminal includes these pre-defined aliases:

```cmd
ll      = dir /A         # Detailed listing
la      = dir /A         # All files
l       = dir            # Simple listing
cd..    = cd ..          # Go up (no space needed)
```

---

## Windows-Specific Tips

### Use Windows Command Prompt Shortcuts

```cmd
py-terminal

REM System info
systeminfo              # Full system details
tasklist                # Running processes
wmic os get name,version # OS version
whoami                  # Current user

REM Network
ipconfig                # Network configuration
ping google.com         # Test connectivity
nslookup google.com     # DNS lookup
netstat                 # Network statistics

REM Storage
dir C:\                 # List drives
diskpart                # Disk management

exit
```

### Python Development

```cmd
py-terminal

REM Create virtual environment
python -m venv myenv
myenv\Scripts\activate

REM Install packages
pip install numpy
pip install pandas

REM Run scripts
python script.py
python -m pytest

exit
```

### Git Operations

```cmd
py-terminal

git clone <repo-url>
cd project
git status
git add .
git commit -m "message"
git push

exit
```

---

## Troubleshooting in 30 Seconds

### Problem: "py-terminal not found"

```cmd
REM Solution 1: Close and reopen Command Prompt
REM Solution 2: Check PATH
echo %PATH%

REM Solution 3: Run with full path
python "%APPDATA%\Python-Terminal\terminal_windows.py"

REM Solution 4: Update PATH
setx PATH "%APPDATA%\Python-Terminal;%PATH%"
```

### Problem: "Python not found"

```cmd
REM Install Python from python.org
REM Make sure to check "Add Python to PATH"
python --version
```

### Problem: "Permission denied"

```cmd
REM Try running Command Prompt as Administrator
REM Then re-run setup
setup_windows.bat
```

### Problem: Setup Script Won't Run

```cmd
REM Make sure you're in the right directory
cd C:\path\to\STerminal

REM Try running as Administrator
REM Right-click Command Prompt → Run as administrator
setup_windows.bat
```

---

## Advanced Tips

### Run Multiple Commands in Sequence

```cmd
py-terminal << EOF
mkdir test_project
cd test_project
touch file1.txt
touch file2.txt
ls
exit
EOF
```

### Create Desktop Shortcut

1. Right-click Desktop → New → Shortcut
2. Enter: `%APPDATA%\Python-Terminal\py-terminal.bat`
3. Name it: "Python Terminal"
4. Click Finish

### Use in PowerShell

```powershell
# Add to PowerShell profile
Set-Alias -Name pt -Value py-terminal

# Then use
pt
```

---

## What's Inside?

```
py-terminal includes:
✓ mkdir  - Create folders
✓ touch  - Create files
✓ cd     - Navigate folders
✓ ls/dir - List files
✓ pwd    - Show location
✓ cat/type - View files
✓ cp     - Copy files
✓ mv     - Move files
✓ rm     - Delete files
✓ echo   - Print text
✓ help   - Show commands
✓ history - View history
✓ clear/cls - Clear screen
+ Run any Windows command
```

---

## Common Windows Commands (Also Work)

You can use any Windows command inside py-terminal:

```cmd
py-terminal

REM File and folder operations
dir
cd C:\
mkdir TestFolder
del file.txt

REM System information
systeminfo
tasklist
wmic os get name

REM Network commands
ipconfig
ping
nslookup

REM Process management
tasklist
taskkill /IM app.exe

REM Development tools
python
pip
git
npm
node

exit
```

---

## Cheat Sheet

### Navigation
```cmd
pwd                     # Current folder
cd folder               # Go into folder
cd ..                   # Go up one level
cd C:\                  # Go to root
cd %USERPROFILE%       # Go to home
```

### Files & Folders
```cmd
ls / dir                # List files
mkdir folder            # Create folder
touch file.txt          # Create file
cat / type file.txt     # View file
cp file1 file2          # Copy
mv file1 file2          # Move/rename
rm file.txt             # Delete file
rm -r folder            # Delete folder
```

### Help & Control
```cmd
help                    # Show commands
history                 # Show history
clear / cls             # Clear screen
exit                    # Exit terminal
```

---

## Next Steps

1. **Explore Help**: Run `help` inside terminal
2. **Read Full Guide**: Check README_WINDOWS.md
3. **Learn More**: See INSTALL_WINDOWS.md
4. **Practice**: Create test folders and files

---

## Quick Reference Card

**Start**: `py-terminal`  
**Help**: `help`  
**Exit**: `exit`  

**Make Folder**: `mkdir name`  
**Make File**: `touch name.txt`  
**List Files**: `ls` or `dir`  
**View File**: `cat file.txt`  
**Copy**: `cp file1 file2`  
**Move**: `mv file1 path\file2`  
**Delete**: `rm file.txt`  
**Navigate**: `cd folder`  
**Back**: `cd ..`  
**Show Path**: `pwd`  

---

## FAQ

**Q: Is it safe?**  
A: Yes! It runs with your user permissions only.

**Q: Can I run my scripts?**  
A: Yes! Run `python script.py` inside.

**Q: How is it different from Command Prompt?**  
A: It has custom commands and a cleaner interface, great for learning.

**Q: Can I uninstall it?**  
A: Yes! Delete the Python-Terminal folder from AppData.

**Q: Does it work on Windows 7/8?**  
A: Yes! Tested on Windows 7, 8, 10, and 11.

---

## Useful Websites

- Python: https://python.org
- Windows Terminal: https://github.com/microsoft/terminal
- Git: https://git-scm.com
- Node.js: https://nodejs.org

---

## More Help

- **Installation help**: See INSTALL_WINDOWS.md
- **Features list**: See README_WINDOWS.md
- **Full documentation**: Check the .md files
- **In-terminal help**: Type `help`

---

**Happy Terminal-ing on Windows!** 🚀

*Last Updated: 2024*
