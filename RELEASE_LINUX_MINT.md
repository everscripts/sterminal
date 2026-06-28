# Linux Mint Portable Release

## Build and package

Run the following from the project root:

```bash
bash package_linux.sh
bash publish_linux_release.sh
```

This creates:
- dist/release/stterminal-linux-portable.tar.gz
- dist/release/stterminal-linux-portable/

## How users run it

Extract the archive and run:

```bash
./run_stterminal.sh
```

## Where to upload

Best options:
- GitHub Releases: https://github.com/everscripts/sterminal/releases
- SourceForge: https://sourceforge.net/
- Any direct-download file host
