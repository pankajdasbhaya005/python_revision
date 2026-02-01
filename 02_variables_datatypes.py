# Variables and Data Types in Python
# This file explains variables and all basic data types with examples

# 1. Variables
# Variable is a name that stores a value in memory

name = "pankaj"
age = 20
height = 5.4
is_student = True

print(name)
print(age)
print(height)
print(is_student)

# Output:
# Babu
# 21
# 5.8
# True


# 2. Checking data type using type()

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

# Output:
# <class 'str'>
# <class 'int'>
# <class 'float'>
# <class 'bool'>


# 3. Integer (int)
# Integer stores whole numbers

a = 10
b = -5
c = 0

print(a, b, c)

# Output:
# 10 -5 0


# 4. Float (float)
# Float stores decimal numbers

x = 3.14
y = 10.0

print(x)
print(y)

# Output:
# 3.14
# 10.0


# 5. String (str)
# String stores text data

message = "Python is easy"
single_char = "A"

print(message)
print(single_char)

# Output:
# Python is easy
# A


# 6. Boolean (bool)
# Boolean has only two values: True or False

is_python_fun = True
is_java_hard = False

print(is_python_fun)
print(is_java_hard)

# Output:
# True
# False


# 7. Multiple variable assignment

a, b, c = 1, 2, 3
print(a)
print(b)
print(c)

# Output:
# 1
# 2
# 3


# 8. Same value to multiple variables

x = y = z = 100
print(x, y, z)

# Output:
# 100 100 100


# 9. Dynamic typing
# Python allows changing data type of a variable

value = 10
print(value)
print(type(value))

value = "Ten"
print(value)
print(type(value))

# Output:
# 10
# <class 'int'>
# Ten
# <class 'str'>
