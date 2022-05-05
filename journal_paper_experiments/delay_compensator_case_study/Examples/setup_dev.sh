#!/usr/bin/env bash

VENV="venv"

echo "Creating virtual environment"
python3 -m venv "$VENV"

echo "Activate virtual env"
source venv/bin/activate

echo "Upgrade pip"
python3 -m pip install --upgrade pip

echo "Install wheel"
pip install wheel

echo "Install python3 packages"
pip install -r requirements.txt

echo "Running all examples"
python3 run_all_examples.py
