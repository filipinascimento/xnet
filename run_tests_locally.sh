#!/bin/bash

# Install dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt

# Run tests
# python -m unittest discover -s tests -p "*_test.py"
# The tests are in the tests folder
python -m unittest discover -s tests -p "*_test.py" -v