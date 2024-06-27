#!/bin/bash

# Check if Python is installed
if ! command -v python3 &> /dev/null
then
    echo "Python 3 is not installed. Please install Python 3.x and try again."
    exit 1
fi

# Create virtual environment if it does not exist
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install requests

echo "Setup complete. Virtual environment and dependencies have been installed."
