# Tuples in Python
# Tuple is a collection of multiple values
# Tuple is ordered but NOT changeable (immutable)

# 1. Creating a tuple
numbers = (10, 20, 30)
names = ("pankaj", "Amit", "Ravi")

print(numbers)
print(names)

# Output:
# (10, 20, 30)
# ('pankaj', 'Amit', 'Ravi')


# 2. Accessing tuple elements
print(numbers[0])
print(numbers[-1])

# Output:
# 10
# 30


# 3. Tuple is immutable (cannot change value)
# numbers[1] = 25   # This will give error


# 4. Tuple slicing
print(numbers[1:])
print(numbers[:2])

# Output:
# (20, 30)
# (10, 20)


# 5. Tuple with one element (important)
single = (10,)
print(type(single))

# Output:
# <class 'tuple'>


# 6. Tuple methods (very limited)

data = (1, 2, 2, 3, 4)

print(data.count(2))
print(data.index(3))

# Output:
# 2
# 3


# 7. Converting tuple to list
t = (1, 2, 3)
lst = list(t)

lst.append(4)
print(lst)

# Output:
# [1, 2, 3, 4]
