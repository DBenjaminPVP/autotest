#!/bin/bash

# setup.sh
# This script sets up the Python virtual environment and installs dependencies.

# Exit immediately if a command exits with a non-zero status.
set -e

echo "🚀 Starting project setup for macOS..."

# 1. Create a Python virtual environment named 'venv'
echo "-> Creating virtual environment in 'venv/'..."
python3 -m venv venv

# 2. Activate the virtual environment
source venv/bin/activate

# 3. Install Python packages from requirements.txt
echo "-> Installing dependencies from requirements.txt..."
pip install -r requirements.txt

# 4. Install the Playwright browser binaries
echo "-> Installing Playwright browsers..."
playwright install

echo ""
echo "✅ Setup complete!"
echo "If you are not using VSCODE, activate the virtual environment in your terminal by running:"
echo "-> source venv/bin/activate"
echo "If you are using VSCODE, open the Command Palette:"
echo "-> Cmd + Shift + P"
echo "Type Python: Select Interpreter and select it"
echo "Click on the one inside the project: ./venv/bin/python"