#!/bin/bash

# update_project.sh
# This script automates the update process for system and project dependencies.

# Exit immediately if a command exits with a non-zero status.
set -e

echo "🚀 Starting project update process..."

# --- 1. Update Homebrew System Dependencies ---
echo ""
echo "-> Updating Homebrew and upgrading formulae..."
brew update
brew upgrade

# --- 2. Update Python Project Dependencies ---
# Define the path to the pip executable inside your virtual environment
VENV_PIP="venv/bin/pip"

echo ""
echo "-> Upgrading Python packages in the virtual environment..."

# Check if the venv pip exists before trying to use it
if [ ! -f "$VENV_PIP" ]; then
    echo "Error: Virtual environment pip not found at $VENV_PIP"
    echo "Please run the setup.sh script first."
    exit 1
fi

# Use the venv's pip to install the latest versions of all packages
# listed in requirements.txt. The --upgrade flag is the key here.
"$VENV_PIP" install --upgrade -r requirements.txt

echo ""
echo "✅ Project update complete!"
echo "All Homebrew and Python packages have been upgraded to their latest versions."