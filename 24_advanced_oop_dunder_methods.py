# Advanced OOP in Python: Dunder (Magic) Methods
# Dunder methods start and end with double underscores (__)

# 1. Why dunder methods?
# They define how objects behave with:
# print(), len(), +, ==, for loop, etc.


# 2. __str__ and __repr__
# __str__  -> user-friendly string
# __repr__ -> developer/debug-friendly string

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"User(name={self.name}, age={self.age})"

    def __repr__(self):
        return f"User('{self.name}', {self.age})"

u = User("pankaj", 20)
print(u)
print(repr(u))

# Output:
# User(name=pankaj, age=20)
# User('pankaj', 20)


# 3. __len__
# Allows using len() on object

class Playlist:
    def __init__(self, songs):
        self.songs = songs

    def __len__(self):
        return len(self.songs)

p = Playlist(["song1", "song2", "song3"])
print(len(p))

# Output:
# 3


# 4. Operator overloading (__add__)
# Allows using + with custom objects

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

p1 = Point(2, 3)
p2 = Point(4, 5)

print(p1 + p2)

# Output:
# (6, 8)


# 5. Comparison operators (__eq__, __lt__)
class Student:
    def __init__(self, marks):
        self.marks = marks

    def __eq__(self, other):
        return self.marks == other.marks

    def __lt__(self, other):
        return self.marks < other.marks

s1 = Student(80)
s2 = Student(90)

print(s1 == s2)
print(s1 < s2)

# Output:
# False
# True


# 6. __getitem__ and __setitem__
# Allows object to behave like list/dict

class MyList:
    def __init__(self, items):
        self.items = items

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value

ml = MyList([10, 20, 30])
print(ml[1])

ml[1] = 99
print(ml.items)

# Output:
# 20
# [10, 99, 30]


# 7. __iter__ (object becomes iterable)

class Counter:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.limit:
            self.current += 1
            return self.current
        else:
            raise StopIteration

for i in Counter(3):
    print(i)

# Output:
# 1
# 2
# 3


# 8. __call__
# Makes object callable like a function

class Greeter:
    def __call__(self, name):
        print("Hello", name)

g = Greeter()
g("pankaj")

# Output:
# Hello pankaj
