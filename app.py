import unittest

def add(a, b):
    return a + b

class TestApp(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(10, 40), 50)

if __name__ == "__main__":
    print("Python Application Running")
    print("Sum =", add(10, 40))
