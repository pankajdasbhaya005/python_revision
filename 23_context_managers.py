# Context Managers in Python
# Context managers are used to manage resources safely
# Example: files, database connections, locks

# 1. Problem without context manager
# File open -> work -> close (manual)
file = open("demo.txt", "w")
file.write("Hello Context Manager")
file.close()

# Risk:
# - Error aaye to file close na ho


# 2. Using with statement (BEST PRACTICE)
# with automatically handles open and close

with open("demo.txt", "r") as file:
    content = file.read()
    print(content)

# Output:
# Hello Context Manager


# 3. Why with is better?
# - Cleaner code
# - No memory leak
# - Safe even if error occurs


# 4. What happens internally?
# with calls:
# __enter__() when block starts
# __exit__() when block ends


# 5. Creating your own context manager (class based)

class MyContext:
    def __enter__(self):
        print("Entering the context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context")

with MyContext():
    print("Inside context")

# Output:
# Entering the context
# Inside context
# Exiting the context


# 6. Context manager with error handling

class SafeContext:
    def __enter__(self):
        print("Start")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("End")
        if exc_type:
            print("Error handled:", exc_value)
        return True   # suppress error

with SafeContext():
    print(10 / 0)

# Output:
# Start
# End
# Error handled: division by zero


# 7. Context manager using contextlib (EASIER WAY)

from contextlib import contextmanager

@contextmanager
def my_context():
    print("Before")
    yield
    print("After")

with my_context():
    print("Inside block")

# Output:
# Before
# Inside block
# After


# 8. Real example: timing code execution

import time
from contextlib import contextmanager

@contextmanager
def timer():
    start = time.time()
    yield
    end = time.time()
    print("Time taken:", end - start)

with timer():
    for i in range(1000000):
        pass

# Output (example):
# Time taken: 0.05


# 9. Real example: file handling with context manager

@contextmanager
def open_file(filename, mode):
    file = open(filename, mode)
    try:
        yield file
    finally:
        file.close()

with open_file("demo2.txt", "w") as f:
    f.write("Context manager file example")

# Output:
# (file written safely)
