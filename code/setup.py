#!/usr/bin/env python3
"""
Setup script for HackerRank Orchestrate Support Ticket Triage Agent.

Installs dependencies and prepares the environment.
"""

import subprocess
import sys
from pathlib import Path

def run_command(cmd, description):
    """Run a shell command and report status."""
    print(f"→ {description}...")
    result = subprocess.run(cmd, shell=True, capture_output=False)
    if result.returncode != 0:
        print(f"✗ Failed: {description}")
        sys.exit(1)
    print(f"✓ {description}")

def main():
    """Main setup."""
    print("=== HackerRank Orchestrate Setup ===\n")
    
    # Check Python version
    if sys.version_info < (3, 9):
        print("✗ Python 3.9+ required")
        sys.exit(1)
    print(f"✓ Python {sys.version.split()[0]}")
    
    # Create logging directory
    log_dir = Path.home() / "hackerrank_orchestrate"
    log_dir.mkdir(exist_ok=True)
    print(f"✓ Log directory: {log_dir}")
    
    # Install dependencies
    print("\nInstalling dependencies...")
    run_command(f"{sys.executable} -m pip install --upgrade pip", "Upgrade pip")
    run_command(f"{sys.executable} -m pip install -r requirements.txt", "Install packages")
    
    print("\n=== Setup Complete ===")
    print("\nQuick start:")
    print(f"  python main.py")

if __name__ == "__main__":
    main()
