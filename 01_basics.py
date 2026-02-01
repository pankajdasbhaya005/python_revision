# Python Basics
# This file covers very basic concepts of Python

# 1. Printing output
print("Hello World!")
print("Welcome to Python basics")


# 2. Variables
# Variables are used to store data
name = "pankaj"
age = 20
is_student = True

print(name)
print(age)
print(is_student)


# 3. Data types
# type() is used to check the data type

print(type(name))       # string
print(type(age))        # integer
print(type(is_student)) # boolean


# 4. Basic arithmetic operations
a = 10
b = 3

print(a + b)  # addition
print(a - b)  # subtraction
print(a * b)  # multiplication
print(a / b)  # division
print(a % b)  # modulus (remainder)


# 5. Taking input from user
# input() always returns string

user_name = input("Enter your name: ")
print("Hello", user_name)


# 6. Type casting
# Converting one data type to another

num1 = "5"
num2 = "10"

# converting string to integer
result = int(num1) + int(num2)
print(result)
