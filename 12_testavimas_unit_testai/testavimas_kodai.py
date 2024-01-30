import unittest

class TestAsserMethods(unittest.TestCase):
    def test_assertEqual(self):
        self.assertEqual(3 + 2, 5, 'klaidingas atsakymas')


if __name__=="__maina__":
    unittest.main()