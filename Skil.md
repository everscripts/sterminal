# Python Terminal for Linux Mint

## Prompt
Create a Python script that simulates a lightweight terminal interface for Linux Mint.  
The terminal should support:
- Creating folders (directories)
- Creating files inside those folders
- Executing simple commands interactively

## Requirements
- Use Python 3
- Provide a text‑based interface (CLI)
- Allow user input for commands like `mkdir <folder>`, `touch <file>`, and `exit`
- Ensure created files/folders are stored in the current working directory
- Handle invalid commands gracefully with error messages
- the Terminal should support default terminal feature also.
## Example Implementation

```python
import os

def terminal():
    print("Custom Python Terminal (Linux Mint)")
    print("Commands: mkdir <folder>, touch <file>, exit")

    while True:
        cmd = input(">>> ").strip().split()

        if not cmd:
            continue

        if cmd[0] == "mkdir" and len(cmd) == 2:
            try:
                os.makedirs(cmd[1], exist_ok=True)
                print(f"Folder '{cmd[1]}' created.")
            except Exception as e:
                print(f"Error: {e}")

        elif cmd[0] == "touch" and len(cmd) == 2:
            try:
                with open(cmd[1], "w") as f:
                    pass
                print(f"File '{cmd[1]}' created.")
            except Exception as e:
                print(f"Error: {e}")

        elif cmd[0] == "exit":
            print("Exiting terminal...")
            break

        else:
            print("Invalid command. Use mkdir <folder>, touch <file>, exit.")

if __name__ == "__main__":
    terminal()
