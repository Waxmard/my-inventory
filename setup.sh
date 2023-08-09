#!/bin/bash

echo "Setting up my-inventory project..."
chmod +x my-inventory
sudo ln -s "$(pwd)/my-inventory" /usr/local/bin
echo "my-inventory command now runs project!"

echo "Checking for Python3.11..."
if ! command -v python3.11 &> /dev/null
then
    echo "Python3.11 is required. Please install it first."
    exit 1
fi

echo "Setting up virtual environment..."
python3.11 -m venv .venv

echo "Installing required packages..."
source .venv/bin/activate
pip install --upgrade pip
if [[ -f requirements.txt ]]; then
    pip install -r requirements.txt
fi

echo "Virtual environment setup is complete."
echo "To activate the virtual environment, run 'source .venv/bin/activate'"
