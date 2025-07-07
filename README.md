# lazygit-python

A Python clone of lazygit with terminal UI for Git operations.

## 🚀 Quick Start

```bash
python -m lazygit
```

## Features

- 📁 File staging/unstaging with visual status indicators
- 📝 Commit creation with message editor
- 🌿 Branch management (create, checkout, delete)
- 🔄 Push/Pull/Fetch operations
- 📊 Repository status overview
- 📜 Commit history viewer
- 🔍 Diff viewer for files and commits
- 💾 Stash management
- 🔀 Merge and rebase operations
- ⌨️  Keyboard-driven interface

## Installation

### Method 1: Install from source (recommended)

```bash
# Clone the repository
git clone <repository-url>
cd lazygit-python

# Install using pip
pip install .

# Or install in development mode
pip install -e .
```

### Method 2: Install from PyPI (when available)

```bash
pip install lazygit-python
```

### Method 3: Standalone Installers

Download pre-built installers for your platform:

#### Windows
- Download `lazygit-python-0.1.0-setup.exe` from releases
- Run the installer and follow the setup wizard
- The application will be available in Start Menu and Desktop

#### macOS
- Download `lazygit-python-0.1.0.dmg` from releases
- Open the DMG and drag the app to Applications
- Run from Applications or use `lazygit-py` in terminal

#### Linux
- **AppImage**: Download `lazygit-python-0.1.0-x86_64.AppImage`, make executable with `chmod +x`, and run
- **Debian/Ubuntu**: Download `lazygit-python_0.1.0_all.deb` and install with `sudo dpkg -i`
- **Snap**: `sudo snap install lazygit-python` (when available)

### Method 4: Build from source

```bash
# Clone and enter directory
git clone <repository-url>
cd lazygit-python

# Build standalone executable
make installer

# Or build specific format
python build_installers.py [pyinstaller|windows|macos|linux]
```

## Usage

Run from within a git repository:

```bash
# If installed via pip or installer
lazygit-py

# Short alias
lgpy

# Or run directly with Python
python -m lazygit
```

## Keyboard Shortcuts

### Navigation
- `Tab` - Next panel
- `Shift+Tab` - Previous panel
- `↑/↓` - Navigate items
- `q` - Quit

### Files
- `s` - Stage/Unstage selected file
- `a` - Stage all files
- `u` - Unstage all files
- `D` - View diff of selected file

### Commits
- `c` - Create commit
- `Enter` - Show commit details

### Branches
- `b` - Checkout branch
- `n` - Create new branch
- `d` - Delete branch
- `m` - Merge selected branch
- `R` - Rebase onto selected branch

### Remote Operations
- `p` - Push
- `P` - Pull
- `f` - Fetch

### Stash
- `S` - Stash changes
- `Ctrl+S` - Pop latest stash

### Other
- `r` - Refresh
- `?` - Show help

## Requirements

- Python 3.8+
- Git installed and accessible from command line
- Terminal with Unicode support

## Dependencies

- `textual` - Terminal UI framework
- `GitPython` - Git operations
- `click` - CLI framework
- `pyyaml` - Configuration support

## Project Structure

```
lazygit-python/
├── lazygit/
│   ├── __init__.py
│   ├── __main__.py
│   ├── git_operations.py    # Git command wrapper
│   └── ui/
│       ├── __init__.py
│       ├── app.py           # Main TUI application
│       └── dialogs.py       # Dialog components
├── requirements.txt
├── setup.py
└── README.md
```

## Limitations

- Some advanced Git features are not yet implemented
- Remote branch deletion is not supported from the UI
- Interactive rebase is not supported
- Cherry-pick is not implemented

## License

This is a educational project inspired by the original lazygit.