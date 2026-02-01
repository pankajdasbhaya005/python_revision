# Strings in Python
# This file explains string basics, operations and methods with outputs

# 1. Creating strings
name = "pankaj"
city = 'jsg'

print(name)
print(city)

# Output:
# pankaj
# jsg


# 2. Multi-line string
message = """Python is easy.
Python is powerful.
Python is popular."""

print(message)

# Output:
# Python is easy.
# Python is powerful.
# Python is popular.


# 3. String length
text = "Python"
print(len(text))

# Output:
# 6


# 4. Accessing characters (indexing)
word = "Python"

print(word[0])
print(word[1])
print(word[-1])

# Output:
# P
# y
# n


# 5. String slicing
print(word[0:4])
print(word[2:])
print(word[:3])

# Output:
# Pyth
# thon
# Pyt


# 6. String concatenation
first_name = "pankaj"
last_name = "Dasbhaya"

full_name = first_name + " " + last_name
print(full_name)

# Output:
# pankaj Dasbhaya


# 7. String repetition
text = "Hi"
print(text * 3)

# Output:
# Hi Hi Hi 


# 8. String methods (commonly used)
sentence = "python is easy"

print(sentence.upper())
print(sentence.lower())
print(sentence.capitalize())
print(sentence.title())

# Output:
# PYTHON IS EASY
# python is easy
# Python is easy
# Python Is Easy


# 9. Removing extra spaces
data = "  hello world "

print(data.strip())
print(data.lstrip())
print(data.rstrip())

# Output:
# hello world
# hello world 
#   hello world


# 10. Replacing text
msg = "I like Java"
print(msg.replace("Java", "Python"))

# Output:
# I like Python


# 11. Checking string content
text = "Python123"

print(text.isalpha())
print(text.isdigit())
print(text.isalnum())

# Output:
# False
# False
# True


# 12. String formatting (f-string)
name = "pankaj"
age = 20

print(f"My name is {name} and my age is {age}")

# Output:
# My name is pankaj and my age is 20
