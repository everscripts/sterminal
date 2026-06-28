from pathlib import Path
import shutil
import tarfile
import os

SCRIPT_DIR = Path(__file__).resolve().parent
DIST_LINUX = SCRIPT_DIR / "dist" / "linux"
RELEASE_DIR = SCRIPT_DIR / "dist" / "release" / "stterminal-linux-portable"
TAR_PATH = SCRIPT_DIR / "dist" / "release" / "stterminal-linux-portable.tar.gz"

RELEASE_DIR.mkdir(parents=True, exist_ok=True)
if RELEASE_DIR.exists():
    for child in RELEASE_DIR.iterdir():
        if child.is_dir():
            shutil.rmtree(child)
        else:
            child.unlink()

files_to_copy = [
    "terminal.py",
    "terminal_gui.py",
    "terminal_windows.py",
    "validate_system.py",
    "requirements.txt",
    "setup_linux_mint.sh",
    "package_linux.sh",
    "README.md",
    "INSTALL_LINUX_MINT.md",
    "QUICKSTART.md",
]

for name in files_to_copy:
    src = SCRIPT_DIR / name
    if src.exists():
        shutil.copy2(src, RELEASE_DIR / name)

if (DIST_LINUX / "stterminal").exists():
    shutil.copy2(DIST_LINUX / "stterminal", RELEASE_DIR / "stterminal")
if (DIST_LINUX / "stterminal-gui").exists():
    shutil.copy2(DIST_LINUX / "stterminal-gui", RELEASE_DIR / "stterminal-gui")

launcher = RELEASE_DIR / "run_stterminal.sh"
launcher.write_text(
    "#!/bin/bash\n"
    "set -euo pipefail\n"
    'DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"\n'
    'if [ -x "$DIR/stterminal" ]; then "$DIR/stterminal" "$@"; elif [ -x "$DIR/stterminal-gui" ]; then "$DIR/stterminal-gui" "$@"; else python3 "$DIR/terminal.py" "$@"; fi\n',
    encoding="utf-8"
)
launcher.chmod(0o755)

with tarfile.open(TAR_PATH, "w:gz") as tar:
    for entry in RELEASE_DIR.iterdir():
        tar.add(entry, arcname=entry.name)

print(f"Portable Linux release created at: {TAR_PATH}")
print(f"Release folder: {RELEASE_DIR}")
