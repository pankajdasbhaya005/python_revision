# Exception Handling in Python
# Exception handling is used to handle runtime errors
# So that program does not crash


# 1. Simple error example (without handling)
# print(10 / 0)
# Output:
# ZeroDivisionError



# 2. try and except
# try -> risky code
# except -> runs if error occurs

try:
    print(10 / 0)
except:
    print("Error occurred: Division by zero")

# Output:
# Error occurred: Division by zero



# 3. Handling specific exception
try:
    num = int("abc")
except ValueError:
    print("ValueError: Invalid number")

# Output:
# ValueError: Invalid number



# 4. Multiple except blocks
try:
    x = int(input("Enter a number: "))
    print(10 / x)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Please enter a valid number")

# Output (example):
# Enter a number: 0
# Cannot divide by zero



# 5. else block
# else runs if NO exception occurs
try:
    x = int(input("Enter a number: "))
    print(10 / x)
except Exception:
    print("Error occurred")
else:
    print("Division successful")

# Output (example):
# Enter a number: 2
# 5.0
# Division successful



# 6. finally block
# finally always runs (error ho ya na ho)
try:
    file = open("test.txt", "r")
except FileNotFoundError:
    print("File not found")
finally:
    print("This block always executes")

# Output:
# File not found
# This block always executes



# 7. Using except Exception as e
try:
    print(10 / 0)
except Exception as e:
    print("Error:", e)

# Output:
# Error: division by zero



# 8. Raising exception manually
age = -5

if age < 0:
    raise ValueError("Age cannot be negative")

# Output:
# ValueError: Age cannot be negative
