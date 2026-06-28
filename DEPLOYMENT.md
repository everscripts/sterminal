# Deployment Guide for Linux Mint

## Overview

This guide provides comprehensive instructions for deploying Python Terminal across Linux Mint systems, from single-user installations to organization-wide deployments.

---

## Deployment Scenarios

### Scenario 1: Single User Installation (Home Lab)

**Target**: Individual user on personal computer

#### Steps

```bash
# 1. Download files
wget <repository-url>/STerminal.zip
unzip STerminal.zip && cd STerminal

# 2. Run setup
bash setup_linux_mint.sh

# 3. Reload shell
source ~/.bashrc

# 4. Verify
py-terminal
help
exit
```

**Time**: 2-3 minutes  
**Privileges**: User-level only  
**Recovery**: Delete `~/.local/share/python-terminal/`

---

### Scenario 2: Multiple Users (Shared System)

**Target**: Multiple users on same Linux Mint machine

#### System Administrator Steps

```bash
# 1. Download as root
cd /tmp
wget <repository-url>/STerminal.zip
unzip STerminal.zip && cd STerminal

# 2. Install system-wide
sudo cp terminal.py /usr/local/bin/py-terminal
sudo chmod 755 /usr/local/bin/py-terminal

# 3. Verify
which py-terminal
py-terminal --version
```

#### Per-User Configuration

Each user can create custom aliases:

```bash
# Add to ~/.bashrc
echo "alias pyterm='py-terminal'" >> ~/.bashrc
source ~/.bashrc
```

**Privileges**: Root-level (one-time)  
**Recovery**: `sudo rm /usr/local/bin/py-terminal`

---

### Scenario 3: Organization Deployment

**Target**: Multiple machines across organization

#### Prerequisites

- Access to package repository or central server
- Linux Mint deployment infrastructure
- System administration team

#### Deployment Methods

##### Method A: Using Configuration Management (Ansible)

```yaml
---
- hosts: all_linux_mint_systems
  tasks:
    - name: Create installation directory
      file:
        path: /opt/python-terminal
        state: directory
        mode: '0755'
    
    - name: Copy terminal application
      copy:
        src: terminal.py
        dest: /opt/python-terminal/terminal.py
        mode: '0755'
    
    - name: Create symlink
      file:
        src: /opt/python-terminal/terminal.py
        dest: /usr/local/bin/py-terminal
        state: link
    
    - name: Update PATH for all users
      lineinfile:
        path: /etc/profile.d/python-terminal.sh
        line: 'export PATH="/usr/local/bin:$PATH"'
        create: yes
```

Run deployment:
```bash
ansible-playbook deploy.yml -i inventory.ini
```

##### Method B: Using APT Package (Debian/Ubuntu)

Create a package:

```bash
# Create package structure
mkdir -p python-terminal_1.0/usr/local/bin
mkdir -p python-terminal_1.0/DEBIAN

# Copy application
cp terminal.py python-terminal_1.0/usr/local/bin/py-terminal
chmod 755 python-terminal_1.0/usr/local/bin/py-terminal

# Create control file
cat > python-terminal_1.0/DEBIAN/control << EOF
Package: python-terminal
Version: 1.0
Section: utils
Priority: optional
Architecture: all
Depends: python3 (>= 3.6)
Maintainer: Your Organization
Description: Python Terminal Emulator for Linux Mint
 A lightweight terminal interface built in Python
 for Linux Mint systems.
EOF

# Build package
dpkg-deb --build python-terminal_1.0

# Install on systems
sudo dpkg -i python-terminal_1.0.deb
```

##### Method C: Using Docker (Containerized)

```dockerfile
FROM ubuntu:22.04

RUN apt-get update && apt-get install -y python3 python3-pip

WORKDIR /app
COPY terminal.py /app/
RUN chmod +x /app/terminal.py

ENTRYPOINT ["/app/terminal.py"]
```

Build and deploy:
```bash
docker build -t python-terminal:1.0 .
docker push your-registry.com/python-terminal:1.0
```

---

## Installation Verification

### Test Installation

```bash
# Verify executable
which py-terminal

# Check Python version
python3 --version

# Test execution
py-terminal << EOF
help
exit
EOF

# Check in system
py-terminal -v 2>/dev/null || echo "Check manual"
```

### Automated Testing Script

```bash
#!/bin/bash
# test_terminal.sh

echo "Testing Python Terminal Installation..."

# Test 1: Command exists
if command -v py-terminal &> /dev/null; then
    echo "✓ Terminal command found"
else
    echo "✗ Terminal command not found"
    exit 1
fi

# Test 2: Python available
if python3 --version &> /dev/null; then
    echo "✓ Python 3 available"
else
    echo "✗ Python 3 not found"
    exit 1
fi

# Test 3: Help command works
output=$(echo "help" | py-terminal 2>&1 | head -1)
if [ ! -z "$output" ]; then
    echo "✓ Terminal responds to commands"
else
    echo "✗ Terminal not responding"
    exit 1
fi

echo "✓ All tests passed"
```

---

## Upgrade Procedure

### In-Place Upgrade

```bash
# Backup current version
cp /usr/local/bin/py-terminal /usr/local/bin/py-terminal.backup

# Update application
sudo cp terminal.py /usr/local/bin/py-terminal
sudo chmod 755 /usr/local/bin/py-terminal

# Test
py-terminal -v

# If issues, rollback
sudo cp /usr/local/bin/py-terminal.backup /usr/local/bin/py-terminal
```

### Blue-Green Deployment

```bash
# Install new version alongside old
sudo cp terminal.py /usr/local/bin/py-terminal-v2.0
sudo chmod 755 /usr/local/bin/py-terminal-v2.0

# Test v2.0
py-terminal-v2.0

# Switch symlink
sudo rm /usr/local/bin/py-terminal
sudo ln -s /usr/local/bin/py-terminal-v2.0 /usr/local/bin/py-terminal

# Verify
py-terminal

# Remove old version after testing period
sudo rm /usr/local/bin/py-terminal-v1.0
```

---

## Rollback Procedures

### If Installation Fails

```bash
# Remove installation
sudo rm /usr/local/bin/py-terminal
sudo rm -rf /opt/python-terminal

# Verify removal
which py-terminal  # Should not find

# Reinstall from backup
sudo cp backup/terminal.py /usr/local/bin/py-terminal
sudo chmod 755 /usr/local/bin/py-terminal
```

### User-Level Rollback

```bash
# For user installations
rm ~/.local/bin/py-terminal
rm -rf ~/.local/share/python-terminal/

# Verify
py-terminal  # Should not find
```

---

## Monitoring & Maintenance

### Health Check Script

```bash
#!/bin/bash
# monitor_terminal.sh

LOG_FILE="/var/log/py-terminal-health.log"

{
    echo "=== Health Check: $(date) ==="
    
    # Check if installed
    if command -v py-terminal &> /dev/null; then
        echo "✓ Terminal installed"
    else
        echo "✗ Terminal NOT installed"
    fi
    
    # Check Python
    if python3 --version &> /dev/null; then
        python3 --version | xargs echo "✓ Python:"
    else
        echo "✗ Python not available"
    fi
    
    # Check permissions
    ls -la $(which py-terminal) 2>/dev/null || echo "✗ Permission issue"
    
    # Test run
    if echo "exit" | py-terminal &> /dev/null; then
        echo "✓ Terminal executes"
    else
        echo "✗ Terminal failed to execute"
    fi
    
} >> "$LOG_FILE"
```

Schedule with cron:

```bash
# Check every day at 2 AM
0 2 * * * /usr/local/bin/monitor_terminal.sh
```

---

## Troubleshooting Deployment Issues

### Issue: Command Not Found After Installation

```bash
# Check PATH
echo $PATH

# Check installation location
ls -la /usr/local/bin/py-terminal

# Verify permissions
stat /usr/local/bin/py-terminal

# Force reload
exec bash
```

### Issue: Python Module Errors

```bash
# Check Python version
python3 --version

# Verify Python installation
python3 -c "import sys; print(sys.path)"

# Reinstall Python if needed
sudo apt install --reinstall python3
```

### Issue: Permission Denied on Shared System

```bash
# Check file ownership
ls -l /usr/local/bin/py-terminal

# Fix permissions (admin)
sudo chmod 755 /usr/local/bin/py-terminal
sudo chown root:root /usr/local/bin/py-terminal
```

---

## Performance Considerations

### Resource Requirements

- **Disk Space**: ~150 KB
- **Memory (Runtime)**: 10-15 MB baseline
- **CPU**: Minimal (task dependent)
- **Python Version**: 3.6+

### Optimization Tips

1. **Minimize History**: Limit command history in large deployments
2. **Use Symlinks**: Reduces disk space with multiple installations
3. **Centralize Logs**: Forward logs to central monitoring

---

## Security Deployment Considerations

### Access Control

```bash
# Restrict access (if needed)
sudo chmod 750 /usr/local/bin/py-terminal  # Only user/group can execute

# Create user group
sudo groupadd python-terminal-users
sudo usermod -aG python-terminal-users username
```

### Audit Logging

```bash
# Log all terminal executions
sudo auditctl -w /usr/local/bin/py-terminal -p x -k terminal_execution
```

### Security Updates

```bash
# When updating for security issues
sudo apt update
sudo apt install python3  # Update Python runtime

# Update terminal
sudo cp terminal.py /usr/local/bin/py-terminal
```

---

## Post-Deployment

### User Training

Provide documentation:
- README.md for features
- Quick reference guide
- Video tutorials (optional)

### Feedback Collection

```bash
# Send feedback survey to users
cat > feedback.txt << EOF
How would you rate Python Terminal?
1. Poor
2. Fair
3. Good
4. Excellent

Comments: ___________________
EOF
```

### Maintenance Schedule

- **Weekly**: Health checks
- **Monthly**: Review logs and feedback
- **Quarterly**: Update to latest Python 3 version
- **Annually**: Major review and optimization

---

## Rollout Timeline Example

### Week 1: Pilot
- Deploy to 10 test systems
- Collect feedback
- Run stability tests

### Week 2: Early Adoption
- Deploy to 50 systems
- Monitor performance
- Address issues

### Week 3: Standard Rollout
- Deploy to 200+ systems
- Establish support procedures
- Document lessons learned

### Week 4: Complete Deployment
- Final systems
- Cleanup and documentation
- Archive for future reference

---

## Support & Escalation

### Support Levels

**Level 1** (User Self-Service)
- Documentation access
- Help command
- Basic troubleshooting

**Level 2** (System Administrator)
- Installation issues
- Permission problems
- Performance tuning

**Level 3** (Development Team)
- Bug reports
- Feature requests
- Code-level debugging

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

---

**Last Updated**: 2024  
**Version**: 1.0  
**Compatibility**: Linux Mint 19.x - 21.x
