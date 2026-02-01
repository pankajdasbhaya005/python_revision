# Important String Methods in Python
# Covers commonly used and important string methods with outputs

# 1. upper() and lower()
text = "Python Is Easy"

print(text.upper())
print(text.lower())

# Output:
# PYTHON IS EASY
# python is easy


# 2. capitalize() and title()
sentence = "python is very powerful"

print(sentence.capitalize())
print(sentence.title())

# Output:
# Python is very powerful
# Python Is Very Powerful


# 3. strip(), lstrip(), rstrip()
data = "   hello python   "

print(data.strip())
print(data.lstrip())
print(data.rstrip())

# Output:
# hello python
# hello python   
#    hello python


# 4. replace()
msg = "I love Java"
print(msg.replace("Java", "Python"))

# Output:
# I love Python


# 5. find() and index()
text = "python programming"

print(text.find("p"))
print(text.find("z"))
print(text.index("p"))

# Output:
# 0
# -1
# 0


# 6. count()
text = "banana"
print(text.count("a"))

# Output:
# 3


# 7. startswith() and endswith()
filename = "data.csv"

print(filename.startswith("data"))
print(filename.endswith(".csv"))

# Output:
# True
# True


# 8. split()
sentence = "Python is very easy"
words = sentence.split()

print(words)

# Output:
# ['Python', 'is', 'very', 'easy']


# 9. join()
words = ["Python", "is", "awesome"]
sentence = " ".join(words)

print(sentence)

# Output:
# Python is awesome


# 10. isupper(), islower()
text = "PYTHON"
print(text.isupper())
print(text.islower())

# Output:
# True
# False


# 11. isnumeric(), isdigit(), isdecimal()
num = "123"

print(num.isnumeric())
print(num.isdigit())
print(num.isdecimal())

# Output:
# True
# True
# True


# 12. format()
name = "Babu"
age = 21

print("My name is {} and age is {}".format(name, age))

# Output:
# My name is Babu and age is 21
