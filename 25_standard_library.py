# Python Standard Library - Most Useful Modules
# These modules come built-in with Python

# 1. datetime module
from datetime import datetime, date, timedelta

now = datetime.now()
print("Current Date & Time:", now)

today = date.today()
print("Today's Date:", today)

# Adding days
future = today + timedelta(days=5)
print("After 5 days:", future)

# Formatting date
formatted = now.strftime("%d-%m-%Y %H:%M:%S")
print("Formatted:", formatted)

# Output (example):
# Current Date & Time: 2026-02-11 23:40:00
# Today's Date: 2026-02-11
# After 5 days: 2026-02-16
# Formatted: 11-02-2026 23:40:00


# 2. os module
import os

print("Current Working Directory:", os.getcwd())

# List files
print("Files in folder:", os.listdir())

# Check if file exists
print("Does demo.txt exist?", os.path.exists("demo.txt"))

# Output (example):
# Current Working Directory: /home/user/project
# Files in folder: ['file1.py', 'demo.txt']
# Does demo.txt exist? True


# 3. sys module
import sys

print("Python version:", sys.version)
print("Command line arguments:", sys.argv)

# Output (example):
# Python version: 3.x.x
# Command line arguments: ['25_standard_library.py']


# 4. json module

import json

data = {
    "name": "pankaj",
    "age": 20,
    "city": "jsg"
}

# Convert Python dict -> JSON string
json_data = json.dumps(data)
print("JSON string:", json_data)

# Convert JSON string -> Python dict
parsed_data = json.loads(json_data)
print("Back to dict:", parsed_data)

# Output:
# JSON string: {"name": "pankaj", "age": 20, "city": "jsg"}
# Back to dict: {'name': 'pankaj', 'age': 20, 'city': 'jsg'}


# 5. collections module

from collections import Counter, defaultdict

# Counter - counts frequency
nums = [1, 2, 2, 3, 3, 3]
count = Counter(nums)
print("Counter:", count)

# defaultdict - avoids key error
d = defaultdict(int)
d["a"] += 1
d["b"] += 2
print("Defaultdict:", d)

# Output:
# Counter: Counter({3: 3, 2: 2, 1: 1})
# Defaultdict: defaultdict(<class 'int'>, {'a': 1, 'b': 2})
