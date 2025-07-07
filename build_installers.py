#!/usr/bin/env python3
"""
Build platform-specific installers for lazygit-python
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def build_with_pyinstaller():
    """Build standalone executable with PyInstaller"""
    print("Building standalone executable with PyInstaller...")
    
    # Install PyInstaller if not present
    subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller"], check=True)
    
    # Create spec file content
    spec_content = """
# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['lazygit/__main__.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=['textual', 'GitPython', 'click', 'yaml'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='lazygit-py',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
"""
    
    with open("lazygit-py.spec", "w") as f:
        f.write(spec_content)
    
    # Build the executable
    subprocess.run(["pyinstaller", "lazygit-py.spec", "--clean"], check=True)
    
    print(f"Executable built in: dist/lazygit-py")

def build_windows_installer():
    """Build Windows installer using NSIS"""
    if sys.platform != "win32":
        print("Windows installer can only be built on Windows")
        return
    
    nsis_script = """
!define PRODUCT_NAME "Lazygit Python"
!define PRODUCT_VERSION "0.1.0"
!define PRODUCT_PUBLISHER "Your Name"
!define PRODUCT_DIR_REGKEY "Software\\Microsoft\\Windows\\CurrentVersion\\App Paths\\lazygit-py.exe"

SetCompressor lzma

Name "${PRODUCT_NAME} ${PRODUCT_VERSION}"
OutFile "lazygit-python-${PRODUCT_VERSION}-setup.exe"
InstallDir "$PROGRAMFILES\\Lazygit Python"
InstallDirRegKey HKLM "${PRODUCT_DIR_REGKEY}" ""
ShowInstDetails show
ShowUnInstDetails show

Section "MainSection" SEC01
  SetOutPath "$INSTDIR"
  SetOverwrite ifnewer
  File "dist\\lazygit-py.exe"
  CreateDirectory "$SMPROGRAMS\\Lazygit Python"
  CreateShortCut "$SMPROGRAMS\\Lazygit Python\\Lazygit Python.lnk" "$INSTDIR\\lazygit-py.exe"
  CreateShortCut "$DESKTOP\\Lazygit Python.lnk" "$INSTDIR\\lazygit-py.exe"
SectionEnd

Section -AdditionalIcons
  CreateShortCut "$SMPROGRAMS\\Lazygit Python\\Uninstall.lnk" "$INSTDIR\\uninst.exe"
SectionEnd

Section -Post
  WriteUninstaller "$INSTDIR\\uninst.exe"
  WriteRegStr HKLM "${PRODUCT_DIR_REGKEY}" "" "$INSTDIR\\lazygit-py.exe"
  WriteRegStr HKLM "Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\${PRODUCT_NAME}" "DisplayName" "$(^Name)"
  WriteRegStr HKLM "Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\${PRODUCT_NAME}" "UninstallString" "$INSTDIR\\uninst.exe"
  WriteRegStr HKLM "Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\${PRODUCT_NAME}" "DisplayIcon" "$INSTDIR\\lazygit-py.exe"
  WriteRegStr HKLM "Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\${PRODUCT_NAME}" "DisplayVersion" "${PRODUCT_VERSION}"
  WriteRegStr HKLM "Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\${PRODUCT_NAME}" "Publisher" "${PRODUCT_PUBLISHER}"
SectionEnd

Section Uninstall
  Delete "$INSTDIR\\uninst.exe"
  Delete "$INSTDIR\\lazygit-py.exe"
  Delete "$SMPROGRAMS\\Lazygit Python\\Uninstall.lnk"
  Delete "$DESKTOP\\Lazygit Python.lnk"
  Delete "$SMPROGRAMS\\Lazygit Python\\Lazygit Python.lnk"
  RMDir "$SMPROGRAMS\\Lazygit Python"
  RMDir "$INSTDIR"
  DeleteRegKey HKLM "Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\${PRODUCT_NAME}"
  DeleteRegKey HKLM "${PRODUCT_DIR_REGKEY}"
  SetAutoClose true
SectionEnd
"""
    
    with open("installer.nsi", "w") as f:
        f.write(nsis_script)
    
    print("NSIS script created. Run 'makensis installer.nsi' to build Windows installer")

def build_macos_app():
    """Build macOS .app bundle"""
    if sys.platform != "darwin":
        print("macOS app can only be built on macOS")
        return
    
    print("Building macOS app bundle...")
    
    # First build with PyInstaller
    build_with_pyinstaller()
    
    # Create DMG installer script
    dmg_script = """#!/bin/bash
# Create a DMG installer for macOS

APP_NAME="Lazygit Python"
VERSION="0.1.0"
DMG_NAME="lazygit-python-${VERSION}.dmg"
VOLUME_NAME="Lazygit Python ${VERSION}"

# Create a temporary directory
TEMP_DIR=$(mktemp -d)
cp -r "dist/lazygit-py" "$TEMP_DIR/"

# Create DMG
hdiutil create -volname "$VOLUME_NAME" -srcfolder "$TEMP_DIR" -ov -format UDZO "$DMG_NAME"

# Clean up
rm -rf "$TEMP_DIR"

echo "DMG created: $DMG_NAME"
"""
    
    with open("create_dmg.sh", "w") as f:
        f.write(dmg_script)
    
    os.chmod("create_dmg.sh", 0o755)
    print("DMG creation script created. Run './create_dmg.sh' to build macOS installer")

def build_linux_packages():
    """Build Linux packages (deb, rpm, AppImage)"""
    if sys.platform not in ["linux", "linux2"]:
        print("Linux packages can only be built on Linux")
        return
    
    # Create debian package structure
    debian_dir = Path("debian")
    debian_dir.mkdir(exist_ok=True)
    
    control_content = """Package: lazygit-python
Version: 0.1.0
Section: utils
Priority: optional
Architecture: all
Depends: python3 (>= 3.8), python3-pip
Maintainer: Your Name <your.email@example.com>
Description: A Python clone of lazygit with TUI interface
 Lazygit Python is a terminal UI for git commands, inspired by lazygit.
 It provides an intuitive interface for common git operations.
"""
    
    (debian_dir / "control").write_text(control_content)
    
    # Create AppImage build script
    appimage_script = """#!/bin/bash
# Build AppImage for lazygit-python

# First build with PyInstaller
python3 -m PyInstaller --onefile --name lazygit-py lazygit/__main__.py

# Download appimagetool if not present
if [ ! -f appimagetool-x86_64.AppImage ]; then
    wget https://github.com/AppImage/AppImageKit/releases/download/continuous/appimagetool-x86_64.AppImage
    chmod +x appimagetool-x86_64.AppImage
fi

# Create AppDir structure
mkdir -p AppDir/usr/bin
cp dist/lazygit-py AppDir/usr/bin/

# Create desktop entry
cat > AppDir/lazygit-python.desktop <<EOF
[Desktop Entry]
Type=Application
Name=Lazygit Python
Exec=lazygit-py
Icon=lazygit-python
Categories=Development;
Comment=A Python clone of lazygit with TUI interface
EOF

# Create AppRun
cat > AppDir/AppRun <<EOF
#!/bin/bash
HERE="\\$(dirname "\\$(readlink -f "\\${0}")")"
exec "\\${HERE}/usr/bin/lazygit-py" "\\$@"
EOF
chmod +x AppDir/AppRun

# Build AppImage
./appimagetool-x86_64.AppImage AppDir lazygit-python-0.1.0-x86_64.AppImage

echo "AppImage created: lazygit-python-0.1.0-x86_64.AppImage"
"""
    
    with open("build_appimage.sh", "w") as f:
        f.write(appimage_script)
    
    os.chmod("build_appimage.sh", 0o755)
    print("AppImage build script created. Run './build_appimage.sh' to build AppImage")

def main():
    """Main build function"""
    print("Lazygit Python Installer Builder")
    print("================================")
    
    if len(sys.argv) > 1:
        target = sys.argv[1]
        if target == "pyinstaller":
            build_with_pyinstaller()
        elif target == "windows":
            build_windows_installer()
        elif target == "macos":
            build_macos_app()
        elif target == "linux":
            build_linux_packages()
        else:
            print(f"Unknown target: {target}")
            print("Available targets: pyinstaller, windows, macos, linux")
    else:
        # Build for current platform
        build_with_pyinstaller()
        
        if sys.platform == "win32":
            build_windows_installer()
        elif sys.platform == "darwin":
            build_macos_app()
        elif sys.platform in ["linux", "linux2"]:
            build_linux_packages()

if __name__ == "__main__":
    main()