# Loops in Python
# Loops are used to repeat a block of code multiple times
# Python mainly has two loops: for loop and while loop


# 1. while loop
# while loop runs as long as the condition is True
count = 1

while count <= 5:
    print(count)
    count += 1   # important to avoid infinite loop

# Output:
# 1
# 2
# 3
# 4
# 5


# 2. while loop with else
# else runs when loop condition becomes False normally

num = 1

while num <= 3:
    print(num)
    num += 1
else:
    print("Loop finished")

# Output:
# 1
# 2
# 3
# Loop finished


# 3. for loop (basic)
# for loop is used to iterate over a sequence

for i in range(5):
    print(i)

# Output:
# 0
# 1
# 2
# 3
# 4


# 4. for loop with range(start, end)

for i in range(1, 6):
    print(i)

# Output:
# 1
# 2
# 3
# 4
# 5


# 5. for loop with step

for i in range(1, 11, 2):
    print(i)

# Output:
# 1
# 3
# 5
# 7
# 9


# 6. for loop iterating over list

fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)

# Output:
# apple
# banana
# mango


# 7. for loop iterating over string

word = "Python"

for char in word:
    print(char)

# Output:
# P
# y
# t
# h
# o
# n


# 8. for loop with dictionary

student = {"name": "pankaj", "age": 20}

for key in student:
    print(key, student[key])

# Output:
# name pankaj
# age 20


# 9. for loop with else
# else runs if loop completes normally (no break)

for i in range(3):
    print(i)
else:
    print("Loop completed successfully")

# Output:
# 0
# 1
# 2
# Loop completed successfully


# 10. break statement
# break stops the loop immediately

for i in range(1, 6):
    if i == 3:
        break
    print(i)

# Output:
# 1
# 2


# 11. continue statement
# continue skips the current iteration

for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# Output:
# 1
# 2
# 4
# 5


# 12. break with for-else (important)

for i in range(1, 6):
    if i == 3:
        break
    print(i)
else:
    print("This will NOT run")

# Output:
# 1
# 2


# 13. pass statement
# pass means "do nothing"
# used as placeholder

for i in range(3):
    pass

print("Loop executed with pass")

# Output:
# Loop executed with pass
