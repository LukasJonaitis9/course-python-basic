import unittest


class TestAssertMethods(unittest.TestCase):
    def test_assertEqual(self):
        self.assertEqual(3 + 2, 5)


if __name__ == 'main':
    unittest.main()