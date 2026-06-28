# Windows Release Publishing

## Build and package

Run the following from the project root:

```bat
package_windows.bat
publish_windows_release.bat
```

This creates:
- dist/release/stterminal-windows-portable.zip
- dist/release/stterminal-windows-portable/

## Where to upload

Best options:
- GitHub Releases: https://github.com/everscripts/sterminal/releases
- SourceForge: https://sourceforge.net/
- Any cloud storage or file host for direct download

## Recommended upload contents

Upload the ZIP file as the downloadable release artifact.

Users can extract it and run:
- stterminal.exe
- stterminal-gui.exe
