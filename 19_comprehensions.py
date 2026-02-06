# Comprehensions in Python
# Comprehensions are short and clean ways to create collections

# 1. Why comprehensions?
# Normal way (using loop)
numbers = []
for i in range(1, 6):
    numbers.append(i)

print(numbers)

# Output:
# [1, 2, 3, 4, 5]


# 2. List comprehension (basic)
# Syntax:
# [expression for item in iterable]
numbers = [i for i in range(1, 6)]
print(numbers)

# Output:
# [1, 2, 3, 4, 5]


# 3. List comprehension with condition
even_numbers = [i for i in range(1, 11) if i % 2 == 0]
print(even_numbers)

# Output:
# [2, 4, 6, 8, 10]


# 4. List comprehension with if-else
# Syntax:
# [expression_if_true if condition else expression_if_false for item in iterable]
result = ["Even" if i % 2 == 0 else "Odd" for i in range(1, 6)]
print(result)

# Output:
# ['Odd', 'Even', 'Odd', 'Even', 'Odd']


# 5. List comprehension with string
word = "Python"
letters = [ch for ch in word]
print(letters)

# Output:
# ['P', 'y', 't', 'h', 'o', 'n']


# 6. Set comprehension
# Removes duplicates automatically

nums = [1, 2, 2, 3, 3, 4, 5]

unique_nums = {i for i in nums}
print(unique_nums)

# Output:
# {1, 2, 3, 4, 5}


# 7. Set comprehension with condition

even_set = {i for i in range(1, 11) if i % 2 == 0}
print(even_set)

# Output:
# {2, 4, 6, 8, 10}


# 8. Dictionary comprehension
# Syntax:
# {key : value for item in iterable}

squares = {i: i * i for i in range(1, 6)}
print(squares)

# Output:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


# 9. Dictionary comprehension with condition

even_squares = {i: i * i for i in range(1, 11) if i % 2 == 0}
print(even_squares)

# Output:
# {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}


# 10. Using comprehension with existing dictionary

students = {"panakj": 85, "lucky": 72, "raj": 90}

passed_students = {name: marks for name, marks in students.items() if marks >= 80}
print(passed_students)

# Output:
# {'panakj': 85, 'raj': 90}
