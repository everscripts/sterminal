# Deployment Guide for Windows

## Overview

This guide provides comprehensive instructions for deploying Python Terminal across Windows systems, from single-user installations to organization-wide deployments.

---

## Deployment Scenarios

### Scenario 1: Single User Installation (Home/Laptop)

**Target**: Individual user on personal Windows computer

#### Steps

```cmd
REM 1. Download files
cd C:\path\to\STerminal

REM 2. Run setup
setup_windows.bat

REM 3. Close and reopen Command Prompt or PowerShell

REM 4. Verify
py-terminal
help
exit
```

**Time**: 2-3 minutes  
**Privileges**: User-level only  
**Recovery**: Delete `%APPDATA%\Python-Terminal\`

---

### Scenario 2: Multiple Users (Shared Computer)

**Target**: Multiple users on same Windows machine

#### System Administrator Steps

```cmd
REM Run Command Prompt as Administrator
REM (Right-click → Run as administrator)

cd C:\Users\Administrator\Downloads\STerminal

REM 1. Create system-wide installation
mkdir "C:\Program Files\Python-Terminal"

REM 2. Copy files
copy terminal_windows.py "C:\Program Files\Python-Terminal\"

REM 3. Create launcher
(
    echo @echo off
    echo python "C:\Program Files\Python-Terminal\terminal_windows.py" %%*
) > "C:\Program Files\Python-Terminal\py-terminal.bat"

REM 4. Add to system PATH
setx /M PATH "C:\Program Files\Python-Terminal;%PATH%"

REM 5. Verify
py-terminal
help
exit
```

**Privileges**: Administrator-level  
**Recovery**: `rmdir /S "C:\Program Files\Python-Terminal"`

Each user can now use:
```cmd
py-terminal
```

---

### Scenario 3: Organization Deployment (100+ Computers)

**Target**: Enterprise deployment across multiple machines

#### Prerequisites

- Access to Group Policy or software distribution
- Windows Active Directory infrastructure
- System administration team

#### Deployment Methods

##### Method A: Group Policy Deployment

1. Create shared network location:
```cmd
\\server\share\python-terminal\terminal_windows.py
\\server\share\python-terminal\py-terminal.bat
```

2. Create batch file for Group Policy:
```batch
@echo off
REM Deploy Python Terminal via Group Policy
mkdir "%ProgramFiles%\Python-Terminal"
copy "\\server\share\python-terminal\terminal_windows.py" "%ProgramFiles%\Python-Terminal\"
copy "\\server\share\python-terminal\py-terminal.bat" "%ProgramFiles%\Python-Terminal\"
setx /M PATH "%ProgramFiles%\Python-Terminal;%PATH%"
```

3. Deploy via Group Policy:
   - Group Policy Editor → User Configuration → Windows Settings → Scripts
   - Add the batch file as a startup script

##### Method B: SCCM (System Center Configuration Manager)

Create an application deployment:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<package>
  <name>Python Terminal for Windows</name>
  <version>1.0</version>
  <source>\\sccm-server\packages\python-terminal</source>
  <installcommand>setup.bat</installcommand>
  <targetOS>Windows 10</targetOS>
  <targetOS>Windows 11</targetOS>
</package>
```

Deploy to collection of computers.

##### Method C: PowerShell Remoting

Deploy to multiple computers:

```powershell
$computers = @("PC1", "PC2", "PC3", "Server1")

foreach ($computer in $computers) {
    Invoke-Command -ComputerName $computer -ScriptBlock {
        mkdir "C:\Program Files\Python-Terminal" -Force
        Copy-Item "\\server\share\terminal_windows.py" -Destination "C:\Program Files\Python-Terminal\"
        setx /M PATH "C:\Program Files\Python-Terminal;%PATH%"
    } -Credential $adminCreds
}
```

##### Method D: Configuration Management (Ansible/Terraform)

```yaml
---
- name: Deploy Python Terminal to Windows
  hosts: windows_servers
  tasks:
    - name: Create installation directory
      win_file:
        path: 'C:\Program Files\Python-Terminal'
        state: directory

    - name: Copy terminal application
      win_copy:
        src: terminal_windows.py
        dest: 'C:\Program Files\Python-Terminal\terminal_windows.py'

    - name: Create batch launcher
      win_template:
        src: py-terminal.bat.j2
        dest: 'C:\Program Files\Python-Terminal\py-terminal.bat'

    - name: Update system PATH
      win_environment:
        name: PATH
        value: 'C:\Program Files\Python-Terminal'
        state: present
        level: machine
      notify: reboot

    - name: reboot
      win_reboot:
```

---

## Installation Verification

### Test Installation

```cmd
REM Verify executable location
where py-terminal

REM Check Python version
python --version

REM Test execution
py-terminal
help
exit

REM Check in system
tasklist | findstr python
```

### Automated Testing Script

Create `test_terminal.bat`:

```batch
@echo off
setlocal enabledelayedexpansion

echo Testing Python Terminal Installation...

REM Test 1: Command exists
where py-terminal >nul 2>&1
if !errorlevel! equ 0 (
    echo [OK] Terminal command found
) else (
    echo [FAIL] Terminal command not found
    exit /b 1
)

REM Test 2: Python available
python --version >nul 2>&1
if !errorlevel! equ 0 (
    echo [OK] Python available
) else (
    echo [FAIL] Python not found
    exit /b 1
)

REM Test 3: Help command works
for /f "delims=" %%a in ('py-terminal ^<^< EOF
help
exit
EOF 2^>nul') do set output=%%a

if not "!output!"=="" (
    echo [OK] Terminal responds to commands
) else (
    echo [FAIL] Terminal not responding
    exit /b 1
)

echo [OK] All tests passed
exit /b 0
```

Run verification:
```cmd
test_terminal.bat
```

---

## Upgrade Procedure

### In-Place Upgrade

```cmd
REM Backup current version
copy "%APPDATA%\Python-Terminal\terminal_windows.py" "%APPDATA%\Python-Terminal\terminal_windows.py.backup"

REM Download new version
REM Copy to installation directory

REM Update application
copy terminal_windows.py "%APPDATA%\Python-Terminal\"

REM Test
py-terminal
help
exit

REM If issues, rollback
copy "%APPDATA%\Python-Terminal\terminal_windows.py.backup" "%APPDATA%\Python-Terminal\terminal_windows.py"
```

### Blue-Green Deployment

```cmd
REM Install new version alongside old
copy terminal_windows.py "%APPDATA%\Python-Terminal\terminal_windows_v2.0.py"

REM Test v2.0
python "%APPDATA%\Python-Terminal\terminal_windows_v2.0.py"

REM Switch batch file to point to v2.0
(
    echo @echo off
    echo python "%APPDATA%\Python-Terminal\terminal_windows_v2.0.py" %%*
) > "%APPDATA%\Python-Terminal\py-terminal.bat"

REM Verify
py-terminal

REM After testing period, remove old version
del "%APPDATA%\Python-Terminal\terminal_windows.py"
ren "%APPDATA%\Python-Terminal\terminal_windows_v2.0.py" terminal_windows.py
```

---

## Rollback Procedures

### If Installation Fails

```cmd
REM Remove installation
del %APPDATA%\Python-Terminal\*.py
rmdir %APPDATA%\Python-Terminal

REM Verify removal
where py-terminal
REM Should not find

REM Reinstall from backup
copy backup\terminal_windows.py %APPDATA%\Python-Terminal\
```

### System-Wide Rollback

```cmd
REM Run as Administrator
rmdir /S /Q "C:\Program Files\Python-Terminal"

REM Restore PATH if needed
setx /M PATH "C:\Program Files\Python-Backup;%PATH%"
```

---

## Monitoring & Maintenance

### Health Check Script

Create `monitor_terminal.ps1`:

```powershell
# Health Check: Python Terminal

$LogFile = "C:\Logs\py-terminal-health.log"

"=== Health Check: $(Get-Date) ===" | Out-File -Append $LogFile

# Check if installed
if (Get-Command py-terminal -ErrorAction SilentlyContinue) {
    "✓ Terminal installed" | Out-File -Append $LogFile
} else {
    "✗ Terminal NOT installed" | Out-File -Append $LogFile
}

# Check Python
try {
    $version = python --version 2>&1
    "✓ Python: $version" | Out-File -Append $LogFile
} catch {
    "✗ Python not available" | Out-File -Append $LogFile
}

# Test run
$test = cmd /c "echo exit | py-terminal 2>&1" | Select-String -Quiet "Python Terminal"
if ($test) {
    "✓ Terminal executes" | Out-File -Append $LogFile
} else {
    "✗ Terminal failed to execute" | Out-File -Append $LogFile
}

"" | Out-File -Append $LogFile
```

Schedule with Task Scheduler:

1. Open Task Scheduler
2. Create Basic Task
3. Name: "Python Terminal Health Check"
4. Trigger: Daily at 2:00 AM
5. Action: Run `powershell.exe C:\Scripts\monitor_terminal.ps1`

---

## Troubleshooting Deployment Issues

### Issue: Command Not Found After Installation

```cmd
REM Check PATH
echo %PATH%

REM Check installation location
dir "%APPDATA%\Python-Terminal"

REM Force PATH refresh
setx PATH "%PATH%"

REM Close all Command Prompt windows
REM Open new Command Prompt

py-terminal
```

### Issue: Python Module Errors

```cmd
REM Check Python version
python --version

REM Verify Python installation
python -c "import sys; print(sys.path)"

REM Reinstall Python if needed
REM Download from python.org and reinstall
```

### Issue: Permission Denied

```cmd
REM Run as Administrator
REM Then re-run setup or deployment

REM Or manually check file permissions
icacls "%APPDATA%\Python-Terminal\terminal_windows.py"
```

### Issue: PATH Not Updating

```cmd
REM Manually update PATH
setx PATH "%APPDATA%\Python-Terminal;%PATH%"

REM Close all terminals
REM Reopen new terminal

echo %PATH%
REM Should show Python-Terminal path
```

---

## Performance Considerations

### Resource Requirements

- **Disk Space**: ~200 KB per installation
- **Memory (Runtime)**: 15-20 MB baseline
- **CPU**: Minimal (task dependent)
- **Python Version**: 3.6+

### Optimization Tips

1. **Minimize Startup Time**: Use warm cache
2. **Network Deployment**: Host on local share
3. **Parallel Deployment**: Use SCCM or Ansible for multiple machines
4. **Batch Operations**: Deploy multiple machines simultaneously

---

## Security Deployment Considerations

### Access Control

```cmd
REM Restrict access (if needed)
icacls "%APPDATA%\Python-Terminal" /grant:r "%USERNAME%":F

REM Create user group
net localgroup "Terminal-Users" /add
REM Add users to group
net localgroup "Terminal-Users" username /add
```

### Audit Logging

Enable audit logging:

1. Open Group Policy Editor
2. Navigate to Computer Configuration → Windows Settings → Security Settings → Audit Policy
3. Enable "Audit Process Creation"
4. Check logs: Event Viewer → Windows Logs → Security

### Security Updates

When updating Python:

```cmd
REM Update Python runtime
REM Download latest from python.org
REM Run installer with settings preserved

REM Update terminal
copy terminal_windows.py "%APPDATA%\Python-Terminal\"

REM Verify
py-terminal
```

---

## Post-Deployment

### User Training

Provide documentation:
- README_WINDOWS.md for features
- QUICKSTART_WINDOWS.md for quick reference
- Video tutorials (optional)
- Help desk contact information

### Feedback Collection

Create feedback survey:

```cmd
REM Email to users
Subject: Python Terminal - Feedback Survey

How would you rate Python Terminal?
[ ] Poor
[ ] Fair
[ ] Good
[ ] Excellent

Comments: ___________________

Please reply to: support@company.com
```

### Maintenance Schedule

- **Weekly**: Health checks via Task Scheduler
- **Monthly**: Review logs and feedback
- **Quarterly**: Update to latest Python 3 version
- **Annually**: Major review and optimization

---

## Rollout Timeline Example

### Week 1: Pilot Phase
- Deploy to 10 IT staff machines
- Collect feedback
- Run stability tests
- Document issues

### Week 2: Early Adoption
- Deploy to 50 power users
- Monitor performance
- Address issues
- Update documentation

### Week 3: Standard Rollout
- Deploy to 200+ machines
- Establish support procedures
- Create FAQ
- Document lessons learned

### Week 4: Complete Deployment
- Deploy to remaining systems
- Finalize support processes
- Archive documentation
- Schedule maintenance

---

## Support & Escalation

### Support Levels

**Level 1** (User Self-Service)
- Documentation access
- Help command (inside terminal)
- Basic troubleshooting guides
- FAQ access

**Level 2** (Help Desk)
- Installation issues
- Permission problems
- PATH configuration
- Basic debugging

**Level 3** (System Administration)
- Performance tuning
- Multi-machine deployment
- Custom configuration
- Integration with other tools

**Level 4** (Development Team)
- Bug reports
- Feature requests
- Code-level debugging
- Performance optimization

---

## Appendix: Deployment Checklist

- [ ] System requirements verified
- [ ] Backup created
- [ ] Installation completed
- [ ] Verification tests passed
- [ ] User documentation provided
- [ ] Support team trained
- [ ] Monitoring configured
- [ ] Rollback procedure documented
- [ ] Deployment logged
- [ ] User feedback collected
- [ ] Success metrics defined
- [ ] Post-deployment review scheduled

---

## Appendix: Command Reference

### Installation Commands

```cmd
REM User installation
setup_windows.bat

REM System-wide installation (as Administrator)
mkdir "C:\Program Files\Python-Terminal"
copy terminal_windows.py "C:\Program Files\Python-Terminal\"
setx /M PATH "C:\Program Files\Python-Terminal;%PATH%"

REM Test
py-terminal
```

### Verification Commands

```cmd
REM Check location
where py-terminal

REM Check version
python --version

REM Test execution
py-terminal
help
exit
```

### Troubleshooting Commands

```cmd
REM Check PATH
echo %PATH%

REM Update PATH
setx PATH "%APPDATA%\Python-Terminal;%PATH%"

REM Remove installation
rmdir /S %APPDATA%\Python-Terminal

REM Check Python
python --version
```

---

## Appendix: Registry Reference

### PATH Registry Location

```
HKEY_CURRENT_USER\Environment\PATH        (User)
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Environment\PATH  (System)
```

### Registry Commands

```cmd
REM Query PATH
reg query HKCU\Environment /v PATH

REM Add to user PATH
setx PATH "%APPDATA%\Python-Terminal;%PATH%"

REM Add to system PATH (Administrator)
setx /M PATH "C:\Program Files\Python-Terminal;%PATH%"
```

---

**Last Updated**: 2024  
**Version**: 1.0  
**Platform**: Windows 7, 8, 10, 11, Server editions
