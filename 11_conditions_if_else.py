# Conditional Expressions in Python (if, elif, else)
# Conditions are used to make decisions in code

# 1. Basic if statement
age = 18

if age >= 18:
    print("You are eligible to vote")

# Output:
# You are eligible to vote


# 2. if-else statement
age = 16

if age >= 18:
    print("You are eligible to vote")
else:
    print("You are NOT eligible to vote")

# Output:
# You are NOT eligible to vote


# 3. if-elif-else statement
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

# Output:
# Grade B


# 4. Comparison operators or relational operators
a = 10
b = 20

print(a == b)   # equal to
print(a != b)   # not equal
print(a > b)    # greater than
print(a < b)    # less than
print(a >= b)   # greater than or equal
print(a <= b)   # less than or equal

# Output:
# False
# True
# False
# True
# False
# True


# 5. Logical operators
x = 10

print(x > 5 and x < 15)
print(x > 5 or x > 20)
print(not(x > 5))

# Output:
# True
# True
# False


# 6. Membership operators
fruits = ["apple", "banana", "mango"]

print("apple" in fruits)
print("grape" not in fruits)

# Output:
# True
# True


# 7. Identity operators
a = 10
b = 10
c = 20

print(a is b)
print(a is not c)

# Output:
# True
# True


# 8. Nested if (if inside if)
num = 10

if num > 0:
    if num % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")

# Output:
# Positive even number


# 9. Short-hand if (conditional expression)
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)

# Output:
# Adult


# 10. Using input with condition
number = int(input("Enter a number: "))

if number > 0:
    print("Positive number")
elif number < 0:
    print("Negative number")
else:
    print("Zero")

# Output (example):
# Enter a number: -5
# Negative number
