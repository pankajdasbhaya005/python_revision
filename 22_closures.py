# Closures in Python
# Closure is a function that remembers variables from its outer scope
# even after the outer function has finished execution

# 1. Simple nested function
def outer():
    message = "Hello"

    def inner():
        print(message)

    inner()

outer()

# Output:
# Hello


# 2. Function returning another function
def outer():
    message = "Hello from outer"

    def inner():
        print(message)

    return inner

func = outer()
func()

# Output:
# Hello from outer


# 3. What is a closure?
# Even though outer() is finished,
# inner() still remembers 'message'

# outer() execution finished,
# but 'message' is still accessible


# 4. Closure with parameter
def make_multiplier(x):
    def multiply(y):
        return x * y
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))
print(triple(5))

# Output:
# 10
# 15


# 5. Multiple closures from same function
def power(n):
    def calculate(x):
        return x ** n
    return calculate

square = power(2)
cube = power(3)

print(square(4))
print(cube(4))

# Output:
# 16
# 64


# 6. Closure vs normal function
def normal_add(x):
    return x + 10

def closure_add(x):
    def add(y):
        return x + y
    return add

add_five = closure_add(5)

print(normal_add(5))
print(add_five(10))

# Output:
# 15
# 15


# 7. nonlocal keyword
# Used to modify outer variable inside inner function
def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

c = counter()

print(c())
print(c())
print(c())

# Output:
# 1
# 2
# 3


# 8. Common mistake (without nonlocal)
def wrong_counter():
    count = 0

    def increment():
        # count += 1   # This will cause error
        return count

    return increment

wc = wrong_counter()
print(wc())

# Output:
# 0
