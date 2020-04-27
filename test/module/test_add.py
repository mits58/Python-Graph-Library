import unittest

from module.add import add


class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)

    def test_add_negative(self):
        self.assertEqual(add(1, -2), -1)

if __name__ == '__main__':
    unittest.main()
