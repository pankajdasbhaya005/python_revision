# Functions in Python
# Function is a block of code that runs only when it is called
# Functions help to avoid repetition and make code reusable


# 1. Simple function (no parameter, no return)
def greet():
    print("Hello, welcome to Python functions")

greet()

# Output:
# Hello, welcome to Python functions


# 2. Function with parameter
def greet_user(name):
    print("Hello", name)

greet_user("pankaj")

# Output:
# Hello pankaj


# 3. Function with multiple parameters
def add(a, b):
    print(a + b)

add(5, 3)

# Output:
# 8


# 4. Function with return value
# return sends result back to function call
def multiply(a, b):
    return a * b

result = multiply(4, 5)
print(result)

# Output:
# 20


# 5. Difference between print and return (VERY IMPORTANT)
def show_sum(a, b):
    print(a + b)

def get_sum(a, b):
    return a + b

show_sum(2, 3)
value = get_sum(2, 3)
print(value)

# Output:
# 5
# 5


# 6. Default parameter
def greet(name="User"):
    print("Hello", name)

greet()
greet("pankaj")

# Output:
# Hello User
# Hello pankaj


# 7. Keyword arguments
def student_info(name, age):
    print("Name:", name)
    print("Age:", age)

student_info(age=20, name="pankaj")

# Output:
# Name: pankaj
# Age: 20


# 8. Arbitrary arguments (*args)
# Used when number of arguments is unknown
def add_numbers(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total

print(add_numbers(1, 2, 3))
print(add_numbers(5, 10, 15, 20))

# Output:
# 6
# 50


# 9. Arbitrary keyword arguments (**kwargs)
def show_details(**info):
    for key, value in info.items():
        print(key, ":", value)

show_details(name="pankaj", age=20, city="jsg")

# Output:
# name : pankaj
# age : 20
# city : jsg


# 10. Function inside function (Nested function)
def outer():
    print("Outer function")

    def inner():
        print("Inner function")

    inner()

outer()

# Output:
# Outer function
# Inner function


# 11. Local vs Global variable
x = 10   # global variable

def my_function():
    x = 5    # local variable
    print(x)

my_function()
print(x)

# Output:
# 5
# 10


# 12. Using global keyword
count = 0

def increase():
    global count
    count += 1

increase()
increase()
print(count)

# Output:
# 2


# 13. Recursion
# Function calling itself
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

# Output:
# 120


# 14. Lambda function
# Small anonymous function
square = lambda x: x * x
print(square(4))

# Output:
# 16


# 15. Docstring
# Used to describe what function does
def add_two_numbers(a, b):
    """
    This function takes two numbers
    and returns their sum
    """
    return a + b

print(add_two_numbers(3, 4))
print(add_two_numbers.__doc__)

# Output:
# 7
# This function takes two numbers
# and returns their sum
