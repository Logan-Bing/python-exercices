import unittest
from hello import say_hello

class TestHello(unittest.TestCase):

    def test_say_hello(self):
        result = say_hello()
        expected = "Hello, World"
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()

    
