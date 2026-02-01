# Dictionary in Python
# Dictionary stores data in key : value pairs
# Dictionary is unordered (logically), changeable (mutable) and does not allow duplicate keys

# 1. Creating a dictionary
student = {
    "name": "pankaj",
    "age": 20,
    "city": "jsg"
}

print(student)

# Output:
# {'name': 'pankaj', 'age': 20, 'city': 'jsg'}


# 2. Accessing values using key
print(student["name"])
print(student["age"])

# Output:
# pankaj
# 20


# 3. Using get() method (safe way)
print(student.get("city"))
print(student.get("marks"))   # key not present

# Output:
# jsg
# None


# 4. Adding new key-value pair
student["marks"] = 85
print(student)

# Output:
# {'name': 'pankaj', 'age': 20, 'city': 'jsg', 'marks': 85}


# 5. Updating existing value
student["age"] = 22
print(student)

# Output:
# {'name': 'pankaj', 'age': 22, 'city': 'Delhi', 'marks': 85}


# 6. Removing items from dictionary

student.pop("city")      # remove by key
print(student)

student.popitem()        # remove last inserted item
print(student)

# Output:
# {'name': 'pankaj', 'age': 22, 'marks': 85}
# {'name': 'pankaj', 'age': 22}


# 7. Dictionary keys, values and items
print(student.keys())
print(student.values())
print(student.items())

# Output:
# dict_keys(['name', 'age'])
# dict_values(['pankaj', 22])
# dict_items([('name', 'pankaj'), ('age', 22)])


# 8. Looping through dictionary
for key in student:
    print(key, student[key])

# Output:
# name pankaj
# age 22


# 9. Loop using items()
for key, value in student.items():
    print(key, ":", value)

# Output:
# name : pankaj
# age : 22


# 10. Checking key existence
print("name" in student)
print("city" in student)

# Output:
# True
# False


# 11. Copy dictionary
data1 = {"a": 1, "b": 2}
data2 = data1.copy()

print(data2)

# Output:
# {'a': 1, 'b': 2}


# 12. clear() method
data1.clear()
print(data1)

# Output:
# {}


# 13. Nested dictionary
students = {
    "student1": {"name": "Amit", "age": 20},
    "student2": {"name": "Ravi", "age": 22}
}

print(students["student1"]["name"])

# Output:
# Amit

# 14. update() method
a = {"x": 1}
b = {"y": 2}

a.update(b)
print(a)

# Output:
# {'x': 1, 'y': 2}
