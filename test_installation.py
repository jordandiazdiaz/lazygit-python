#!/usr/bin/env python3
"""
Test script to verify the lazygit-python installation
"""

import sys
import subprocess

def test_imports():
    print("Testing imports...")
    try:
        from lazygit import __version__
        print(f"✓ lazygit version: {__version__}")
        
        from lazygit.git_operations import GitOperations
        print("✓ GitOperations imported successfully")
        
        from lazygit.ui import LazyGitApp
        print("✓ LazyGitApp imported successfully")
        
        from lazygit.config import Config
        print("✓ Config imported successfully")
        
        return True
    except ImportError as e:
        print(f"✗ Import error: {e}")
        return False

def test_git_operations():
    print("\nTesting Git operations...")
    try:
        from lazygit.git_operations import GitOperations
        git_ops = GitOperations()
        
        if git_ops.is_git_repo():
            print(f"✓ Current directory is a git repository")
            print(f"  Branch: {git_ops.get_current_branch()}")
            print(f"  Remotes: {len(git_ops.get_remotes())} found")
        else:
            print("✓ GitOperations initialized (not in a git repo)")
        
        return True
    except Exception as e:
        print(f"✗ Git operations error: {e}")
        return False

def test_config():
    print("\nTesting configuration...")
    try:
        from lazygit.config import Config
        config = Config()
        
        print(f"✓ Config path: {config.config_path}")
        print(f"✓ Theme color: {config.get('theme.selected_color')}")
        print(f"✓ Quit key: {config.get('keybindings.quit')}")
        
        return True
    except Exception as e:
        print(f"✗ Config error: {e}")
        return False

def main():
    print("lazygit-python Installation Test")
    print("=" * 40)
    
    all_passed = True
    
    all_passed &= test_imports()
    all_passed &= test_git_operations()
    all_passed &= test_config()
    
    print("\n" + "=" * 40)
    if all_passed:
        print("✓ All tests passed!")
        print("\nTo run lazygit-python:")
        print("  python -m lazygit")
        print("\nOr if installed:")
        print("  lazygit-py")
    else:
        print("✗ Some tests failed!")
        print("Please ensure all dependencies are installed:")
        print("  pip install -r requirements.txt")
        sys.exit(1)

if __name__ == "__main__":
    main()