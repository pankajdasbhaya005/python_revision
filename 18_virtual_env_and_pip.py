# Virtual Environment and pip in Python
# This file explains why and how virtual environments are used

# 1. What is pip?
# pip is Python's package manager
# It is used to install, update and remove external libraries

# Example commands (run in terminal, not inside Python):
# pip install requests
# pip uninstall requests
# pip list


# 2. Why virtual environment is needed?
# Problem without virtual environment:
# - Different projects need different library versions
# - Global install causes conflicts

# Virtual environment creates an isolated Python environment
# Each project has its own dependencies


# 3. Creating virtual environment
# Run this in project folder (terminal):

# python -m venv venv

# This creates a folder named "venv"


# 4. Activating virtual environment
# Windows:
# venv\Scripts\activate

# Mac / Linux:
# source venv/bin/activate

# After activation, terminal shows:
# (venv)


# 5. Installing packages inside virtual env
# pip install requests

# This installs package ONLY for this project


# 6. Checking installed packages
# pip list


# 7. Freezing dependencies
# requirements.txt stores exact package versions

# Command:
# pip freeze > requirements.txt


# 8. Installing from requirements.txt
# pip install -r requirements.txt


# 9. Deactivating virtual environment
# deactivate
