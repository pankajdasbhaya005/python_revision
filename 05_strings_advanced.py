# Advanced String Concepts in Python
# Negative slicing, str() function and escape sequences with outputs

# 1. Negative indexing
word = "Python"

print(word[-1])
print(word[-2])
print(word[-6])

# Output:
# n
# o
# P


# 2. Negative slicing
# Format: string[start : end]
# Negative index counts from the end

print(word[-6:-1])
print(word[-4:-1])
print(word[-3:])

# Output:
# Pytho
# tho
# hon


# 3. Mixed slicing (positive + negative)
print(word[1:-1])
print(word[2:-2])

# Output:
# ytho
# th


# 4. Reverse string using slicing
print(word[::-1])

# Output:
# nohtyP


# 5. str() function
# Converts any data type into string

age = 20
marks = 85.5
is_pass = True

print(str(age))
print(str(marks))
print(str(is_pass))

print(type(str(age)))

# Output:
# 20
# 85.5
# True
# <class 'str'>


# 6. Using str() with concatenation
age = 20
message = "My age is " + str(age)
print(message)

# Output:
# My age is 20


# 7. Escape sequences
print("Hello\nWorld")
print("Hello\tWorld")
print("This is a backslash: \\")
print("He said: \"Python is easy\"")

# Output:
# Hello
# World
# Hello    World
# This is a backslash: \
# He said: "Python is easy"


# 8. New line in long text using escape sequence
text = "Python is easy.\nPython is powerful.\nPython is popular."
print(text)

# Output:
# Python is easy.
# Python is powerful.
# Python is popular.
