#!/bin/bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DIST_DIR="$SCRIPT_DIR/dist/linux"
RELEASE_DIR="$SCRIPT_DIR/dist/release/stterminal-linux-portable"
TAR_PATH="$SCRIPT_DIR/dist/release/stterminal-linux-portable.tar.gz"

if [[ ! -f "$DIST_DIR/stterminal" && ! -f "$DIST_DIR/stterminal-gui" ]]; then
  echo "No built Linux executables were found in dist/linux."
  echo "Run package_linux.sh first to build them."
  exit 1
fi

rm -rf "$RELEASE_DIR"
mkdir -p "$RELEASE_DIR" "$SCRIPT_DIR/dist/release"

cp "$DIST_DIR/stterminal" "$RELEASE_DIR/"
cp "$DIST_DIR/stterminal-gui" "$RELEASE_DIR/"
chmod +x "$RELEASE_DIR/stterminal" "$RELEASE_DIR/stterminal-gui"

cat > "$RELEASE_DIR/run_stterminal.sh" <<'EOF'
#!/bin/bash
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
"$DIR/stterminal" "$@"
EOF
chmod +x "$RELEASE_DIR/run_stterminal.sh"

cp "$SCRIPT_DIR/README.md" "$RELEASE_DIR/README.txt"
cp "$SCRIPT_DIR/INSTALL_LINUX_MINT.md" "$RELEASE_DIR/INSTALL.txt"
cp "$SCRIPT_DIR/QUICKSTART.md" "$RELEASE_DIR/QUICKSTART.txt"

tar -czf "$TAR_PATH" -C "$RELEASE_DIR" .

echo "Portable Linux release created successfully."
echo "Archive: $TAR_PATH"
echo "Folder: $RELEASE_DIR"
echo "Upload the .tar.gz file to GitHub Releases, SourceForge, or another download host."
