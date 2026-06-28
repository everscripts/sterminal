# Quick Start Guide - Python Terminal for Linux Mint

> **Get up and running in less than 5 minutes!**

---

## 60-Second Installation

### Step 1: Download
```bash
# Clone or download the STerminal folder
# Open terminal and navigate to the STerminal directory
cd STerminal
```

### Step 2: Install
```bash
bash setup_linux_mint.sh
```

### Step 3: Start
```bash
source ~/.bashrc
py-terminal
```

**Done!** You now have a working Python Terminal. 🎉

---

## Essential Commands

### Create and Navigate

```bash
# Create folders
mkdir projects
cd projects

# Create files
touch README.md
touch script.py

# List contents
ls -la

# Go back
cd ..
```

### View and Edit Files

```bash
# Display file contents
cat README.md

# Show file size
ls -lh script.py
```

### Copy and Move

```bash
# Copy file
cp README.md README.backup

# Move file
mv script.py scripts/

# Remove file
rm README.backup
```

### Get Help

```bash
# Show all commands
help

# Show command history
history

# Exit terminal
exit
```

---

## Common Use Cases

### Scenario 1: Organize Project Files

```bash
py-terminal
mkdir project1
cd project1
mkdir src
mkdir tests
mkdir docs
touch src/main.py
touch tests/test.py
touch README.md
ls -la
exit
```

### Scenario 2: Backup Important Files

```bash
py-terminal
cp myfile.txt myfile.txt.backup
cp myfile.txt.backup ~/backups/
history
exit
```

### Scenario 3: Run Python Scripts

```bash
py-terminal
python3 script.py
python3 script.py --arg1 value1
exit
```

### Scenario 4: Work with Git

```bash
py-terminal
git status
git add .
git commit -m "Initial commit"
exit
```

---

## Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl+C` | Cancel current command |
| `Ctrl+D` | Exit terminal |
| `↑` / `↓` | Navigate history |
| `Tab` | Command history (readline) |
| `Ctrl+L` | Clear screen |

---

## Useful Aliases

Add to `~/.bashrc`:

```bash
# Quick access
alias pt='py-terminal'
alias pyterm='py-terminal'

# Common operations
alias mkdir='mkdir -pv'
alias cp='cp -v'
alias mv='mv -v'
alias rm='rm -v'
```

Then reload:
```bash
source ~/.bashrc
```

---

## Troubleshooting in 30 Seconds

### Problem: "Command not found"

```bash
# Solution 1: Reload shell
source ~/.bashrc

# Solution 2: Use full path
python3 ~/.local/share/python-terminal/terminal.py

# Solution 3: Check Python
python3 --version
```

### Problem: "Permission denied"

```bash
# Fix permissions
chmod +x ~/.local/share/python-terminal/terminal.py
```

### Problem: "Python 3 not found"

```bash
# Install Python
sudo apt update
sudo apt install python3
```

---

## Advanced Tips

### Run Multiple Commands

```bash
py-terminal << EOF
mkdir project
cd project
touch file1.txt
touch file2.txt
ls
exit
EOF
```

### Create Shell Aliases

```bash
# Add to ~/.bashrc
alias myterm='python3 ~/.local/share/python-terminal/terminal.py'

# Then use
myterm
```

### Run in Background

```bash
# Start terminal in background
py-terminal &

# Do other work
# Then bring back
fg
```

---

## What's Inside?

```
py-terminal includes:
✓ mkdir  - Create folders
✓ touch  - Create files
✓ cd     - Navigate folders
✓ ls     - List files
✓ pwd    - Show location
✓ cat    - View files
✓ cp     - Copy files
✓ mv     - Move files
✓ rm     - Delete files
✓ echo   - Print text
✓ help   - Show commands
✓ history - View history
+ Run any Linux command
```

---

## Essential Linux Commands (Also Work)

You can use any Linux command inside py-terminal:

```bash
py-terminal
# File searching
find . -name "*.py"
grep "pattern" file.txt

# File analysis
wc -l script.py
du -sh folder

# System info
whoami
date
uname -a

# Network
ping google.com
wget http://example.com/file.zip

# Text processing
sed 's/old/new/g' file.txt
awk '{print $1}' file.txt

exit
```

---

## Cheat Sheet

### Navigation
```bash
pwd                  # Current directory
cd folder           # Go into folder
cd ..               # Go up one level
cd ~                # Go to home
cd -                # Go to previous
```

### Files & Folders
```bash
ls                  # List files
ls -la              # List all (detailed)
mkdir folder        # Create folder
touch file.txt      # Create file
cat file.txt        # View file
cp file1 file2      # Copy
mv file1 file2      # Move/rename
rm file.txt         # Delete file
rm -r folder        # Delete folder
```

### Help & Exit
```bash
help                # Show commands
history             # Show history
clear               # Clear screen
exit                # Exit terminal
```

---

## Next Steps

1. **Explore Help**: Run `help` inside terminal
2. **Read Full Guide**: Check README.md
3. **Learn More**: See INSTALL_LINUX_MINT.md
4. **Advanced**: Explore DEPLOYMENT.md

---

## Quick Reference Card

**Start**: `py-terminal`  
**Help**: `help`  
**Exit**: `exit`  

**Make Folder**: `mkdir name`  
**Make File**: `touch name.txt`  
**List Files**: `ls`  
**View File**: `cat file.txt`  
**Copy**: `cp file1 file2`  
**Move**: `mv file1 new_location`  
**Delete**: `rm file.txt`  
**Navigate**: `cd folder`  
**Back**: `cd ..`  

---

## FAQ

**Q: Is it safe?**  
A: Yes! It runs with your permissions only.

**Q: Can I run my scripts?**  
A: Yes! Run `python3 script.py` inside.

**Q: Is it like bash?**  
A: Similar but simpler. Perfect for learning.

**Q: Can I uninstall it?**  
A: Yes! See INSTALL_LINUX_MINT.md

**Q: Does it work on Ubuntu?**  
A: Yes! Works on Ubuntu and Debian-based systems.

---

## Useful Websites

- Python: https://python.org
- Linux Mint: https://linuxmint.com
- Ubuntu: https://ubuntu.com
- Debian: https://debian.org

---

## More Help

- **In-terminal help**: Type `help`
- **Full documentation**: See README.md
- **Installation issues**: See INSTALL_LINUX_MINT.md
- **Admin deployment**: See DEPLOYMENT.md

---

**Happy Terminal-ing!** 🚀

*Last Updated: 2024*
