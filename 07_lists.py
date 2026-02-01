# Lists in Python
# List is a collection of multiple values
# List is ordered, changeable (mutable) and allows duplicate values

# 1. Creating a list
numbers = [10, 20, 30, 40]
names = ["pankaj", "Amit", "Ravi"]

print(numbers)
print(names)

# Output:
# [10, 20, 30, 40]
# ['pankaj', 'Amit', 'Ravi']


# 2. Accessing list items (indexing)
print(numbers[0])
print(numbers[-1])

# Output:
# 10
# 40


# 3. Changing list items (list is mutable)
numbers[1] = 25
print(numbers)

# Output:
# [10, 25, 30, 40]


# 4. List slicing
print(numbers[1:3])
print(numbers[:2])
print(numbers[-2:])

# Output:
# [25, 30]
# [10, 25]
# [30, 40]


# 5. Adding elements to list

numbers.append(50)        # adds at the end
numbers.insert(1, 15)     # adds at specific index

print(numbers)

# Output:
# [10, 15, 25, 30, 40, 50]


# 6. Removing elements from list

numbers.remove(25)   # removes specific value
numbers.pop()        # removes last element

print(numbers)

# Output:
# [10, 15, 30, 40]


# 7. Length of list
print(len(numbers))

# Output:
# 4


# 8. Sorting list
nums = [5, 2, 9, 1]

nums.sort()
print(nums)

nums.sort(reverse=True)
print(nums)

# Output:
# [1, 2, 5, 9]
# [9, 5, 2, 1]


# 9. Reverse list
nums.reverse()
print(nums)

# Output:
# [1, 2, 5, 9]


# 10. Copying list
a = [1, 2, 3]
b = a.copy()

print(b)

# Output:
# [1, 2, 3]
