# Modules and Packages in Python
# Modules help to organize code into reusable files

# 1. What is a module?
# Any Python file is a module
# Example: math, random, datetime

import math

print(math.sqrt(16))
print(math.pi)

# Output:
# 4.0
# 3.141592653589793


# 2. Import specific functions
from math import pow

print(pow(2, 3))

# Output:
# 8.0


# 3. Import with alias
import math as m

print(m.factorial(5))

# Output:
# 120


# 4. Using built-in module: random
import random

print(random.randint(1, 10))

# Output (example):
# 7


# 5. Creating your own module
# Create a file: my_module.py
# def greet(name):
#     return f"Hello {name}"

# Usage:
# import my_module
# print(my_module.greet("Babu"))


# 6. What is a package?
# Package = folder containing multiple modules
# Folder must have __init__.py

# structure:
# my_package/
#   __init__.py
#   math_utils.py
#   string_utils.py

# Usage:
# from my_package.math_utils import add
