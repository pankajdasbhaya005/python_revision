# Object Oriented Programming (OOP) in Python
# OOP is based on classes and objects



# 1. What is a class?
# Class is a blueprint or template
# Object is a real instance of a class

class Student:
    pass

# No output (class definition only)


# 2. Creating object of a class
s1 = Student()
print(s1)

# Output (example):
# <__main__.Student object at 0x000001>


# 3. Class with attributes
class Student:
    name = "pankaj"
    age = 20

s1 = Student()
print(s1.name)
print(s1.age)

# Output:
# pankaj
# 20




# 4. __init__ method (constructor)
# __init__ runs automatically when object is created
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("pankaj", 20)
s2 = Student("lucky", 20)

print(s1.name, s1.age)
print(s2.name, s2.age)

# Output:
# pankaj 20
# lucky 20



# 5. What is self?
# self refers to the current object
class Student:
    def show(self):
        print("This is a student")

s1 = Student()
s1.show()

# Output:
# This is a student



# 6. Class with methods
class Calculator:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

calc = Calculator()
print(calc.add(5, 3))
print(calc.multiply(4, 6))

# Output:
# 8
# 24


# 7. Instance variables vs Class variables

class Student:
    university = "IIT MADRAS"   # class variable

    def __init__(self, name):
        self.name = name     # instance variable

s1 = Student("pankaj")
s2 = Student("lucky")

print(s1.name, s1.university)
print(s2.name, s2.university)

# Output:
# pankaj IIT MADRAS
# lucky IIT MADRAS


# 8. Modifying class variable
Student.university = "delhi university"

print(s1.university)
print(s2.university)

# Output:
# delhi university
# delhi university


# 9. Encapsulation (basic idea)
# Protecting data using naming convention
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private variable

    def show_balance(self):
        print("Balance:", self.__balance)

account = BankAccount(5000)
account.show_balance()

# Output:
# Balance: 5000


# 10. Inheritance
# One class inherits another class

class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

dog = Dog()
dog.sound()
dog.bark()

# Output:
# Animal makes sound
# Dog barks


# 11. Method overriding
class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

dog = Dog()
dog.sound()

# Output:
# Dog barks


# 12. Polymorphism
# Same method name, different behavior
class Cat:
    def sound(self):
        print("Cat meows")

class Dog:
    def sound(self):
        print("Dog barks")

animals = [Cat(), Dog()]

for animal in animals:
    animal.sound()

# Output:
# Cat meows
# Dog barks
