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
echo "-> To activate the virtual environment in your terminal, run:"
echo "-> source venv/bin/activate"