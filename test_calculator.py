import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.add(500, 1000), 1500)
        self.assertEqual(self.calculator.add(2, 3), 5)
        self.assertEqual(self.calculator.add(-2, 1), -1)
        self.assertEqual(self.calculator.add(0, 0), 0)

if __name__ == '__main__':
    unittest.main()
