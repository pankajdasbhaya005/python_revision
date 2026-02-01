# Input function in Python
# This file explains how input() works with examples and outputs

# 1. Basic input
name = input("Enter your name: ")
print(name)

# Output (example):
# Enter your name: pankaj
# pankaj


# 2. Input with message
city = input("Enter your city: ")
print("You live in", city)

# Output (example):
# Enter your city: jsg
# You live in jsg


# 3. input() always returns string
age = input("Enter your age: ")
print(age)
print(type(age))

# Output (example):
# Enter your age: 20
# 20
# <class 'str'>


# 4. Converting input to integer (type casting)
age = int(input("Enter your age: "))
print(age)
print(type(age))

# Output (example):
# Enter your age: 20
# 20
# <class 'int'>


# 5. Taking float input
height = float(input("Enter your height: "))
print(height)
print(type(height))

# Output (example):
# Enter your height: 5.4
# 5.4
# <class 'float'>


# 6. Taking multiple inputs using input()
# Values are separated by space

x, y = input("Enter two numbers: ").split()
print(x)
print(y)

# Output (example):
# Enter two numbers: 10 20
# 10
# 20


# 7. Multiple inputs with type casting
a, b = map(int, input("Enter two numbers: ").split())
print(a)
print(b)
print(a + b)

# Output (example):
# Enter two numbers: 5 7
# 5
# 7
# 12
