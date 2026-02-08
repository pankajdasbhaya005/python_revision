# Decorators in Python
# Decorators are used to modify the behavior of a function
# WITHOUT changing the original function code

# 1. Function is an object in Python
def greet():
    print("Hello")

x = greet
x()

# Output:
# Hello


# 2. Function inside another function

def outer():
    print("Outer function")

    def inner():
        print("Inner function")

    inner()

outer()

# Output:
# Outer function
# Inner function


# 3. Function returning another function
def outer():
    def inner():
        print("Hello from inner function")
    return inner

func = outer()
func()

# Output:
# Hello from inner function


# 4. Why decorators are needed?
# Suppose we want to add extra behavior (logging, auth, timing)
# without changing original function
def simple_function():
    print("Original function")

simple_function()

# Output:
# Original function


# 5. Creating a decorator (basic)
def my_decorator(func):
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper


def say_hello():
    print("Hello World")

decorated_func = my_decorator(say_hello)
decorated_func()

# Output:
# Before function execution
# Hello World
# After function execution


# 6. Using @decorator syntax
# This is the clean way
@my_decorator
def say_hi():
    print("Hi everyone")

say_hi()

# Output:
# Before function execution
# Hi everyone
# After function execution


# 7. Decorator with arguments (*args, **kwargs)
def smart_decorator(func):
    def wrapper(*args, **kwargs):
        print("Function name:", func.__name__)
        return func(*args, **kwargs)
    return wrapper


@smart_decorator
def add(a, b):
    return a + b

print(add(3, 4))

# Output:
# Function name: add
# 7


# 8. Real example: login check decorator

def login_required(func):
    def wrapper(user):
        if user == "admin":
            return func(user)
        else:
            print("Access denied")
    return wrapper


@login_required
def dashboard(user):
    print("Welcome to dashboard", user)

dashboard("admin")
dashboard("guest")

# Output:
# Welcome to dashboard admin
# Access denied


# 9. Multiple decorators

def decorator_one(func):
    def wrapper():
        print("Decorator One")
        func()
    return wrapper


def decorator_two(func):
    def wrapper():
        print("Decorator Two")
        func()
    return wrapper


@decorator_one
@decorator_two
def show():
    print("Original function")

show()

# Output:
# Decorator One
# Decorator Two
# Original function
