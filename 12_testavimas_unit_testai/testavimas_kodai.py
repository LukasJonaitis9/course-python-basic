import unittest

def divide(x, y):
    return x / y


class TestAssertMethods(unittest.TestCase):
    def test_assertEqual(self):
        self.assertEqual(3 + 2, 5)

    def test_integer_division(self):
        self.assertEqual(divide(10, 5), 10 // 5)


if __name__ == "__main__":
    unittest.main()