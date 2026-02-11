# Testing Basics in Python
# Testing ensures your code works correctly

# 1. Why testing?
# - Prevent bugs
# - Ensure expected output
# - Safe refactoring
# - Professional practice


# 2. Example function to test
def add(a, b):
    return a + b


# 3. Using unittest (built-in module)
import unittest

class TestMathFunctions(unittest.TestCase):

    def test_add_positive(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative(self):
        self.assertEqual(add(-1, -1), -2)

    def test_add_zero(self):
        self.assertEqual(add(0, 5), 5)


# 4. Running tests
# Run in terminal:
# python 27_testing_basics.py

if __name__ == "__main__":
    unittest.main()
