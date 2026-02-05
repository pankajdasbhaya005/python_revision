# File Handling in Python
# File handling is used to read, write and update files



# 1. Opening a file
# open(filename, mode)
# Modes:
# 'r' -> read
# 'w' -> write (overwrite)
# 'a' -> append
# 'x' -> create
# 'r+' -> read and write



# 2. Writing to a file
file = open("example.txt", "w")
file.write("Hello Python\n")
file.write("This is file handling")
file.close()

# Output:
# (File created: example.txt with written content)


# 3. Reading a file
file = open("example.txt", "r")
content = file.read()
print(content)
file.close()

# Output:
# Hello Python
# This is file handling


# 4. Reading line by line
file = open("example.txt", "r")
print(file.readline())
print(file.readline())
file.close()

# Output:
# Hello Python
# This is file handling


# 5. Reading all lines as list
file = open("example.txt", "r")
lines = file.readlines()
print(lines)
file.close()

# Output:
# ['Hello Python\n', 'This is file handling']


# 6. Append mode
file = open("example.txt", "a")
file.write("\nAppended new line")
file.close()

# Output:
# (New line added at the end of file)


# 7. Using with statement (BEST PRACTICE)
# Automatically closes file
with open("example.txt", "r") as file:
    print(file.read())

# Output:
# Hello Python
# This is file handling
# Appended new line


# 8. File not found handling
try:
    with open("nofile.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File does not exist")

# Output:
# File does not exist


# 9. Checking file exists or not
import os

print(os.path.exists("example.txt"))
print(os.path.exists("random.txt"))

# Output:
# True
# False


# 10. Deleting a file
# os.remove("example.txt")
# print("File deleted")

# Output:
# File deleted
