"""
Python Terminal Emulator for Windows
A lightweight, scalable terminal interface with custom commands and system integration.
Windows-compatible version with full feature parity.
"""

import json
import os
import sys
import platform
import subprocess
import shutil
from pathlib import Path
from typing import List, Optional, Dict, Callable


class TerminalColor:
    """Color codes for Windows terminal output"""
    # Windows 10+ supports ANSI escape codes
    # For older Windows, we use simple text
    SUPPORTS_ANSI = False
    
    @staticmethod
    def _detect_ansi_support():
        """Detect if terminal supports ANSI escape codes"""
        try:
            # Windows 10+ with ANSI support
            if sys.platform == 'win32':
                # Try to enable ANSI support
                os.system('color')  # Initialize color support
                return True
        except:
            pass
        return False
    
    HEADER = '\033[95m' if _detect_ansi_support() else ''
    BLUE = '\033[94m' if _detect_ansi_support() else ''
    CYAN = '\033[96m' if _detect_ansi_support() else ''
    GREEN = '\033[92m' if _detect_ansi_support() else ''
    YELLOW = '\033[93m' if _detect_ansi_support() else ''
    RED = '\033[91m' if _detect_ansi_support() else ''
    WHITE = '\033[97m' if _detect_ansi_support() else ''
    BOLD = '\033[1m' if _detect_ansi_support() else ''
    UNDERLINE = '\033[4m' if _detect_ansi_support() else ''
    END = '\033[0m' if _detect_ansi_support() else ''


class TerminalManager:
    """Manages terminal operations and custom commands for Windows"""
    
    def __init__(self):
        """Initialize terminal manager"""
        self._validate_system()
        self.current_dir = os.getcwd()
        self.history: List[str] = []
        self.saved_commands_file = self._get_saved_commands_path()
        self.saved_commands: Dict[str, str] = self._load_saved_commands()
        self.commands: Dict[str, Callable] = self._setup_commands()
        self.aliases: Dict[str, str] = {
            'll': 'dir /A',
            'la': 'dir /A',
            'l': 'dir',
            'cd..': 'cd ..',
            'clear': 'cls',
            'cat': 'type',
            'grep': 'findstr',
            'pwd': 'cd',
            'ls': 'dir',
            'mkdir': 'md',
            'rm': 'del',
            'rmdir': 'rd',
            'cp': 'copy',
            'mv': 'move',
        }
    
    @staticmethod
    def _validate_system() -> None:
        """Validate that the system is Windows"""
        if sys.platform != 'win32':
            print(f"{TerminalColor.RED}Error: This terminal is compatible only with Windows.{TerminalColor.END}")
            print(f"Current system: {platform.system()}")
            sys.exit(1)
        
        print(f"{TerminalColor.GREEN}✓ Windows system detected{TerminalColor.END}")
        print(f"  Platform: {platform.system()} {platform.release()}")
        print(f"  Python: {platform.python_version()}")
    
    def _setup_commands(self) -> Dict[str, Callable]:
        """Setup custom commands"""
        return {
            'mkdir': self.cmd_mkdir,
            'touch': self.cmd_touch,
            'rmdir': self.cmd_rmdir,
            'rm': self.cmd_rm,
            'ls': self.cmd_ls,
            'pwd': self.cmd_pwd,
            'cd': self.cmd_cd,
            'cat': self.cmd_cat,
            'echo': self.cmd_echo,
            'cp': self.cmd_cp,
            'mv': self.cmd_mv,
            'help': self.cmd_help,
            'savecmd': self.cmd_savecmd,
            'menu': self.cmd_menu,
            'run': self.cmd_run,
            'exit': self.cmd_exit,
            'quit': self.cmd_exit,
            'clear': self.cmd_clear,
            'history': self.cmd_history,
            'dir': self.cmd_ls,
            'type': self.cmd_cat,
        }
    
    def cmd_mkdir(self, args: List[str]) -> None:
        """Create directories"""
        if not args:
            print(f"{TerminalColor.RED}Error: mkdir requires at least one argument{TerminalColor.END}")
            return
        
        for dir_name in args:
            try:
                Path(os.path.join(self.current_dir, dir_name)).mkdir(parents=True, exist_ok=True)
                print(f"{TerminalColor.GREEN}✓ Directory '{dir_name}' created{TerminalColor.END}")
            except Exception as e:
                print(f"{TerminalColor.RED}Error creating '{dir_name}': {e}{TerminalColor.END}")
    
    def cmd_touch(self, args: List[str]) -> None:
        """Create empty files"""
        if not args:
            print(f"{TerminalColor.RED}Error: touch requires at least one argument{TerminalColor.END}")
            return
        
        for file_name in args:
            try:
                file_path = os.path.join(self.current_dir, file_name)
                Path(file_path).touch(exist_ok=True)
                print(f"{TerminalColor.GREEN}✓ File '{file_name}' created{TerminalColor.END}")
            except Exception as e:
                print(f"{TerminalColor.RED}Error creating '{file_name}': {e}{TerminalColor.END}")
    
    def cmd_rmdir(self, args: List[str]) -> None:
        """Remove empty directories"""
        if not args:
            print(f"{TerminalColor.RED}Error: rmdir requires at least one argument{TerminalColor.END}")
            return
        
        for dir_name in args:
            try:
                dir_path = os.path.join(self.current_dir, dir_name)
                os.rmdir(dir_path)
                print(f"{TerminalColor.GREEN}✓ Directory '{dir_name}' removed{TerminalColor.END}")
            except FileNotFoundError:
                print(f"{TerminalColor.RED}Error: Directory '{dir_name}' not found{TerminalColor.END}")
            except OSError as e:
                print(f"{TerminalColor.RED}Error: {e}{TerminalColor.END}")
    
    def cmd_rm(self, args: List[str]) -> None:
        """Remove files or directories"""
        if not args:
            print(f"{TerminalColor.RED}Error: rm requires at least one argument{TerminalColor.END}")
            return
        
        recursive = '-r' in args or '-rf' in args or '/s' in args
        args = [arg for arg in args if arg not in ['-r', '-rf', '/s']]
        
        for target in args:
            try:
                target_path = os.path.join(self.current_dir, target)
                if os.path.isfile(target_path):
                    os.remove(target_path)
                    print(f"{TerminalColor.GREEN}✓ File '{target}' removed{TerminalColor.END}")
                elif os.path.isdir(target_path) and recursive:
                    shutil.rmtree(target_path)
                    print(f"{TerminalColor.GREEN}✓ Directory '{target}' removed{TerminalColor.END}")
                else:
                    print(f"{TerminalColor.RED}Error: Cannot remove '{target}' (use -r for directories){TerminalColor.END}")
            except Exception as e:
                print(f"{TerminalColor.RED}Error: {e}{TerminalColor.END}")
    
    def cmd_ls(self, args: List[str]) -> None:
        """List directory contents (Windows dir equivalent)"""
        try:
            target_dir = self.current_dir
            if args:
                # Check if first arg is a flag
                if args[0].startswith('-') or args[0].startswith('/'):
                    # It's a flag, use with dir
                    dir_flags = args[0]
                    if len(args) > 1:
                        target_dir = os.path.join(self.current_dir, args[1])
                else:
                    target_dir = os.path.join(self.current_dir, args[0])
            
            # List directory
            items = []
            try:
                for item in sorted(os.listdir(target_dir)):
                    item_path = os.path.join(target_dir, item)
                    if os.path.isdir(item_path):
                        items.append(f"[DIR]  {item}")
                    else:
                        size = os.path.getsize(item_path)
                        items.append(f"       {item} ({size} bytes)")
                
                if items:
                    print(f"\nDirectory: {target_dir}\n")
                    for item in items:
                        print(item)
                    print(f"\nTotal items: {len(items)}\n")
                else:
                    print(f"Directory is empty: {target_dir}\n")
            except FileNotFoundError:
                print(f"{TerminalColor.RED}Error: Path not found: {target_dir}{TerminalColor.END}")
        except Exception as e:
            print(f"{TerminalColor.RED}Error: {e}{TerminalColor.END}")
    
    def cmd_pwd(self, args: List[str]) -> None:
        """Print working directory"""
        print(self.current_dir)
    
    def cmd_cd(self, args: List[str]) -> None:
        """Change directory"""
        if not args:
            self.current_dir = os.path.expanduser('~')
        else:
            target = args[0]
            if target == '..' or target == '..\\':
                self.current_dir = os.path.dirname(self.current_dir)
            else:
                target_path = os.path.join(self.current_dir, target)
                if os.path.isdir(target_path):
                    self.current_dir = target_path
                else:
                    print(f"{TerminalColor.RED}Error: Directory '{target}' not found{TerminalColor.END}")
    
    def cmd_cat(self, args: List[str]) -> None:
        """Display file contents"""
        if not args:
            print(f"{TerminalColor.RED}Error: cat requires at least one argument{TerminalColor.END}")
            return
        
        for file_name in args:
            try:
                file_path = os.path.join(self.current_dir, file_name)
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    print(f.read())
            except FileNotFoundError:
                print(f"{TerminalColor.RED}Error: File '{file_name}' not found{TerminalColor.END}")
            except Exception as e:
                print(f"{TerminalColor.RED}Error: {e}{TerminalColor.END}")
    
    def cmd_echo(self, args: List[str]) -> None:
        """Print text"""
        print(' '.join(args))
    
    def cmd_cp(self, args: List[str]) -> None:
        """Copy files or directories"""
        if len(args) < 2:
            print(f"{TerminalColor.RED}Error: cp requires source and destination{TerminalColor.END}")
            return
        
        source = os.path.join(self.current_dir, args[0])
        dest = os.path.join(self.current_dir, args[1])
        
        try:
            if os.path.isfile(source):
                shutil.copy2(source, dest)
                print(f"{TerminalColor.GREEN}✓ File copied{TerminalColor.END}")
            elif os.path.isdir(source):
                shutil.copytree(source, dest)
                print(f"{TerminalColor.GREEN}✓ Directory copied{TerminalColor.END}")
            else:
                print(f"{TerminalColor.RED}Error: Source '{source}' not found{TerminalColor.END}")
        except Exception as e:
            print(f"{TerminalColor.RED}Error: {e}{TerminalColor.END}")
    
    def cmd_mv(self, args: List[str]) -> None:
        """Move files or directories"""
        if len(args) < 2:
            print(f"{TerminalColor.RED}Error: mv requires source and destination{TerminalColor.END}")
            return
        
        source = os.path.join(self.current_dir, args[0])
        dest = os.path.join(self.current_dir, args[1])
        
        try:
            shutil.move(source, dest)
            print(f"{TerminalColor.GREEN}✓ Moved successfully{TerminalColor.END}")
        except Exception as e:
            print(f"{TerminalColor.RED}Error: {e}{TerminalColor.END}")
    
    def cmd_help(self, args: List[str]) -> None:
        """Display available commands"""
        print(f"\n{TerminalColor.BOLD}{TerminalColor.CYAN}Available Commands (Windows):{TerminalColor.END}\n")
        commands_help = {
            'mkdir <dir>': 'Create directory',
            'touch <file>': 'Create file',
            'ls [path]': 'List directory (Windows dir)',
            'cd <path>': 'Change directory',
            'pwd': 'Print working directory',
            'cat <file>': 'Display file (type)',
            'echo <text>': 'Print text',
            'cp <src> <dst>': 'Copy file/directory',
            'mv <src> <dst>': 'Move file/directory',
            'rm [-r] <target>': 'Remove file/directory',
            'rmdir <dir>': 'Remove empty directory',
            'history': 'Show command history',
            'savecmd <name> <cmd>': 'Save a named command',
            'menu list': 'Show saved commands',
            'menu run <name|#>': 'Execute saved command',
            'menu remove <name|#>': 'Remove saved command',
            'run <name|#>': 'Execute saved command',
            'clear': 'Clear screen',
            'help': 'Show this help',
            'exit/quit': 'Exit terminal',
        }
        
        print("Built-in Commands:")
        for cmd, desc in commands_help.items():
            print(f"  {TerminalColor.GREEN}{cmd:<20}{TerminalColor.END} - {desc}")
        
        print(f"\n{TerminalColor.CYAN}Windows Command Examples:{TerminalColor.END}")
        print("  dir              - List files (Windows)")
        print("  type file.txt    - View file (Windows)")
        print("  ipconfig         - Network info")
        print("  tasklist         - Running processes")
        print("  systeminfo       - System information")
        print("  python script.py - Run Python scripts")
        print("  pip install pkg  - Install Python packages")
        print("  git status       - Git operations")
        print()
    
    def cmd_savecmd(self, args: List[str]) -> None:
        """Save a named command for fast execution"""
        if not args:
            print(f"{TerminalColor.RED}Usage: savecmd <name> <command...>{TerminalColor.END}")
            return

        name = args[0]
        if len(args) == 1:
            if not self.history:
                print(f"{TerminalColor.RED}No previous command available to save.{TerminalColor.END}")
                return
            command_to_save = self.history[-1]
        else:
            command_to_save = ' '.join(args[1:])

        self.saved_commands[name] = command_to_save
        self._save_saved_commands()
        print(f"{TerminalColor.GREEN}Saved command '{name}': {command_to_save}{TerminalColor.END}")

    def cmd_menu(self, args: List[str]) -> None:
        """Manage saved command menu entries"""
        if not args or args[0] in ['list', 'show']:
            if not self.saved_commands:
                print(f"{TerminalColor.YELLOW}No saved commands yet. Use savecmd <name> <command...>{TerminalColor.END}")
                return
            print(f"\n{TerminalColor.CYAN}Saved Commands:{TerminalColor.END}")
            for i, (name, command) in enumerate(self.saved_commands.items(), 1):
                print(f"  {i}. {TerminalColor.GREEN}{name}{TerminalColor.END} -> {command}")
            print()
            return

        action = args[0].lower()
        if action in ['help', '?']:
            print(f"\n{TerminalColor.CYAN}Menu command usage:{TerminalColor.END}")
            print("  menu list                 - List saved commands")
            print("  menu run <name|#>         - Execute a saved command")
            print("  menu remove <name|#>      - Remove a saved command")
            print("  savecmd <name> <command>  - Save or update a named command")
            print("  savecmd <name>            - Save last executed command under <name>")
            print()
            return

        if action in ['run', 'exec'] and len(args) > 1:
            self._run_saved_command(args[1])
            return

        if action in ['remove', 'rm', 'delete'] and len(args) > 1:
            self._remove_saved_command(args[1])
            return

        self._run_saved_command(args[0])

    def cmd_run(self, args: List[str]) -> None:
        """Execute a saved command by name or index"""
        if not args:
            print(f"{TerminalColor.RED}Usage: run <name|#>{TerminalColor.END}")
            return
        self._run_saved_command(args[0])

    def _get_saved_commands_path(self) -> str:
        home = os.path.expanduser('~')
        return os.path.join(home, '.sterminal_saved_commands.json')

    def _load_saved_commands(self) -> Dict[str, str]:
        try:
            if os.path.isfile(self.saved_commands_file):
                with open(self.saved_commands_file, 'r', encoding='utf-8') as file:
                    return json.load(file)
        except Exception:
            pass
        return {}

    def _save_saved_commands(self) -> None:
        try:
            with open(self.saved_commands_file, 'w', encoding='utf-8') as file:
                json.dump(self.saved_commands, file, indent=2)
        except Exception as e:
            print(f"{TerminalColor.RED}Error saving menu commands: {e}{TerminalColor.END}")

    def _resolve_saved_command(self, identifier: str) -> Optional[tuple[str, str]]:
        if identifier.isdigit():
            index = int(identifier) - 1
            if 0 <= index < len(self.saved_commands):
                name = list(self.saved_commands.keys())[index]
                return name, self.saved_commands[name]
            return None
        if identifier in self.saved_commands:
            return identifier, self.saved_commands[identifier]
        return None

    def _run_saved_command(self, identifier: str) -> None:
        resolved = self._resolve_saved_command(identifier)
        if not resolved:
            print(f"{TerminalColor.RED}Saved command '{identifier}' not found{TerminalColor.END}")
            return
        name, command = resolved
        print(f"{TerminalColor.CYAN}Running saved command '{name}':{TerminalColor.END} {command}")
        self.process_command(command)

    def _remove_saved_command(self, identifier: str) -> None:
        resolved = self._resolve_saved_command(identifier)
        if not resolved:
            print(f"{TerminalColor.RED}Saved command '{identifier}' not found{TerminalColor.END}")
            return
        name, _ = resolved
        del self.saved_commands[name]
        self._save_saved_commands()
        print(f"{TerminalColor.GREEN}Removed saved command '{name}'{TerminalColor.END}")

    def cmd_history(self, args: List[str]) -> None:
        """Display command history"""
        if not self.history:
            print("No command history yet.")
            return
        
        print(f"\n{TerminalColor.CYAN}Command History:{TerminalColor.END}")
        for i, cmd in enumerate(self.history, 1):
            print(f"  {i}. {cmd}")
        print()
    
    def cmd_clear(self, args: List[str]) -> None:
        """Clear screen"""
        os.system('cls')
    
    def cmd_exit(self, args: List[str]) -> None:
        """Exit terminal"""
        print(f"\n{TerminalColor.YELLOW}Goodbye!{TerminalColor.END}")
        sys.exit(0)
    
    def _execute_system_command(self, cmd: str, args: List[str]) -> None:
        """Execute system command via subprocess"""
        try:
            full_cmd = [cmd] + args
            # Use shell=True for Windows commands
            result = subprocess.run(
                ' '.join(full_cmd),
                cwd=self.current_dir,
                capture_output=True,
                text=True,
                shell=True
            )
            if result.stdout:
                print(result.stdout, end='')
            if result.stderr:
                print(f"{TerminalColor.RED}{result.stderr}{TerminalColor.END}", end='')
        except FileNotFoundError:
            print(f"{TerminalColor.RED}Error: Command '{cmd}' not found{TerminalColor.END}")
        except Exception as e:
            print(f"{TerminalColor.RED}Error: {e}{TerminalColor.END}")
    
    def process_command(self, input_str: str) -> None:
        """Process and execute a command"""
        input_str = input_str.strip()
        
        if not input_str:
            return
        
        # Check for aliases
        parts = input_str.split()
        if parts[0] in self.aliases:
            input_str = self.aliases[parts[0]] + ' ' + ' '.join(parts[1:])
            input_str = input_str.strip()
        
        self.history.append(input_str)
        
        parts = input_str.split(maxsplit=1)
        cmd = parts[0]
        args = parts[1].split() if len(parts) > 1 else []
        
        if cmd in self.commands:
            self.commands[cmd](args)
        else:
            # Try to execute as system command
            self._execute_system_command(cmd, args)
    
    def prompt(self) -> str:
        """Generate terminal prompt"""
        user = os.getenv('USERNAME', 'user')
        computer = os.getenv('COMPUTERNAME', 'WINDOWS')
        short_dir = self.current_dir
        return f"{TerminalColor.GREEN}{user}@{computer}{TerminalColor.END}:{TerminalColor.BLUE}{short_dir}{TerminalColor.END}> "
    
    def run(self) -> None:
        """Start the terminal"""
        print(f"\n{TerminalColor.HEADER}{TerminalColor.BOLD}Python Terminal for Windows{TerminalColor.END}")
        print(f"{TerminalColor.CYAN}Type 'help' for available commands{TerminalColor.END}\n")
        
        try:
            while True:
                try:
                    user_input = input(self.prompt())
                    self.process_command(user_input)
                except KeyboardInterrupt:
                    print(f"\n{TerminalColor.YELLOW}Interrupted by user (Ctrl+C){TerminalColor.END}")
                    break
        except EOFError:
            print(f"\n{TerminalColor.YELLOW}EOF reached{TerminalColor.END}")
            sys.exit(0)


def main():
    """Main entry point"""
    terminal = TerminalManager()
    terminal.run()


if __name__ == '__main__':
    main()
