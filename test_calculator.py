import unittest

class TestCalculator(unittest.TestCase):
    def test_add(self): self.assertEqual(calculator().add(2, 3), 5)
    def test_add(self): self.assertEqual(calculator().add(6, 8), 14)
    def test_add(self): self.assertEqual(calculator().add(8, 9), 17)
    def test_add(self): self.assertEqual(calculator().add(500, 1000), 1500)


