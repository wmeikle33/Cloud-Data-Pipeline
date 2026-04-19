#!/bin/bash

set -e  # exit on error

echo "🚀 Bootstrapping environment..."

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Copy environment variables if not present
if [ ! -f .env ]; then
  cp .env.example .env
  echo "Created .env file"
fi

echo "✅ Setup complete. Activate with: source .venv/bin/activate"
