# Sets in Python
# Set is a collection of unique values
# Set is unordered, mutable, and does NOT allow duplicate elements

# 1. Creating a set
numbers = {1, 2, 3, 4, 4, 5}
print(numbers)

# Output:
# {1, 2, 3, 4, 5}


# 2. Creating empty set (important)
empty_set = set()
print(type(empty_set))

# Output:
# <class 'set'>


# 3. Set properties
# - No duplicate values
# - Unordered (no fixed index)
# - Mutable (can add/remove elements)

# Indexing is NOT allowed in set
# print(numbers[0])  # Error


# 4. Adding elements to set
numbers.add(6)
print(numbers)

# Output:
# {1, 2, 3, 4, 5, 6}


# 5. Updating set with multiple values
numbers.update([7, 8, 9])
print(numbers)

# Output:
# {1, 2, 3, 4, 5, 6, 7, 8, 9}


# 6. Removing elements from set

numbers.remove(3)     # removes element (error if not found)
numbers.discard(10)   # no error if element not found
print(numbers)

# Output:
# {1, 2, 4, 5, 6, 7, 8, 9}


# 7. pop() method
# Removes a random element
removed_item = numbers.pop()
print(removed_item)
print(numbers)

# Output (example):
# 1
# {2, 4, 5, 6, 7, 8, 9}


# 8. clear() method
numbers.clear()
print(numbers)

# Output:
# set()


# 9. Set union
a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))

# Output:
# {1, 2, 3, 4, 5}


# 10. Set intersection
print(a.intersection(b))

# Output:
# {3}


# 11. Set difference
print(a.difference(b))
print(b.difference(a))

# Output:
# {1, 2}
# {4, 5}


# 12. Symmetric difference
print(a.symmetric_difference(b))

# Output:
# {1, 2, 4, 5}


# 13. Subset and Superset
x = {1, 2}
y = {1, 2, 3, 4}

print(x.issubset(y))
print(y.issuperset(x))

# Output:
# True
# True


# 14. Checking membership
print(2 in y)
print(10 in y)

# Output:
# True
# False
