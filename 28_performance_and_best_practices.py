# Performance Optimization and Best Practices in Python 



# 1. Use built-in functions (faster than manual loops)
numbers = [1, 2, 3, 4, 5]

# Slower
total = 0
for n in numbers:
    total += n

# Faster
total_fast = sum(numbers)

print(total_fast)

# Output:
# 15


# 2. Use list comprehension instead of loop when possible

# Slower
squares = []
for i in range(5):
    squares.append(i * i)

# Faster and cleaner
squares_fast = [i * i for i in range(5)]

print(squares_fast)

# Output:
# [0, 1, 4, 9, 16]


# 3. Use set for fast membership checking

nums_list = [1, 2, 3, 4, 5]
nums_set = {1, 2, 3, 4, 5}

print(3 in nums_list)  # Slower
print(3 in nums_set)   # Faster

# Output:
# True
# True


# 4. Avoid unnecessary global variables

# Globals slow down readability and debugging


# 5. Use generator for large data

big_list = [i for i in range(1000000)]
big_gen = (i for i in range(1000000))

print(type(big_gen))

# Output:
# <class 'generator'>


# 6. Use time module for performance testing

import time

start = time.time()

for i in range(1000000):
    pass

end = time.time()

print("Time taken:", end - start)


# 7. Use enumerate instead of manual indexing

names = ["A", "B", "C"]

for index, name in enumerate(names):
    print(index, name)

# Output:
# 0 A
# 1 B
# 2 C


# 8. Use zip for multiple iteration

a = [1, 2, 3]
b = [4, 5, 6]

for x, y in zip(a, b):
    print(x, y)

# Output:
# 1 4
# 2 5
# 3 6
