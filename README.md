# lazygit-python

A Python clone of lazygit with terminal UI for Git operations.

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

```bash
# Clone the repository
git clone <repository-url>
cd lazygit-python

# Install in development mode
pip install -e .

# Or install dependencies directly
pip install -r requirements.txt
```

## Usage

Run from within a git repository:

```bash
# If installed
lazygit-py

# Or run directly
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