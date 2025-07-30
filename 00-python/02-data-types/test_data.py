import unittest
from data_type import return_string, return_integer, return_boolean, return_float

class TestData(unittest.TestCase):

    def test_return_string(self):
        result = return_string()
        self.assertIsInstance(result, str)

    def test_return_integer(self):
        result = return_integer()
        self.assertIsInstance(result, int)

    def test_return_float(self):
        result = return_float()
        self.assertIsInstance(result, float)

    def test_return_boolean(self):
        result = return_boolean()
        self.assertIsInstance(result, bool)

if __name__ == '__main__':
    unittest.main()
