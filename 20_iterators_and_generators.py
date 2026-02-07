# Iterators and Generators in Python
# Used for looping over data in a memory-efficient way

# 1. What is an iterable?
# Iterable = any object you can loop over
# Examples: list, tuple, string, set, dict

numbers = [1, 2, 3]
for n in numbers:
    print(n)

# Output:
# 1
# 2
# 3


# 2. What is an iterator?
# Iterator is an object that remembers its state
# It gives values one by one using next()

nums = [10, 20, 30]
it = iter(nums)

print(next(it))
print(next(it))
print(next(it))

# Output:
# 10
# 20
# 30


# 3. What happens when iterator ends?
# next() raises StopIteration error

# print(next(it))  # StopIteration


# 4. for loop internally uses iterator
# for loop = iter() + next() internally

for x in [5, 6, 7]:
    print(x)

# Output:
# 5
# 6
# 7


# 5. Creating your own iterator
# Using __iter__() and __next__()

class CountUp:
    def __init__(self, max):
        self.max = max
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.max:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration

counter = CountUp(3)

for num in counter:
    print(num)

# Output:
# 1
# 2
# 3


# 6. Why generators?
# Generators are easier way to create iterators
# They use 'yield' instead of 'return'


# 7. Simple generator function

def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()

print(next(gen))
print(next(gen))
print(next(gen))

# Output:
# 1
# 2
# 3


# 8. Generator with loop

def count_up(n):
    i = 1
    while i <= n:
        yield i
        i += 1

for value in count_up(5):
    print(value)

# Output:
# 1
# 2
# 3
# 4
# 5


# 9. Difference between return and yield

def normal_function():
    return 1
    return 2

def generator_function():
    yield 1
    yield 2

print(normal_function())

gen = generator_function()
print(next(gen))
print(next(gen))

# Output:
# 1
# 1
# 2


# 10. Generator expression (like comprehension)
# Uses () instead of []

gen_exp = (i * i for i in range(1, 6))
print(next(gen_exp))
print(next(gen_exp))

# Output:
# 1
# 4


# 11. Memory efficiency example
# List creates all values at once
# Generator creates values one by one

big_list = [i for i in range(1000)]
big_gen = (i for i in range(1000))

print(type(big_list))
print(type(big_gen))

# Output:
# <class 'list'>
# <class 'generator'>
