# creating a calculator module
import unittest
from repository import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(3, 5), -2)
        self.assertEqual(self.calc.subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(0, 5), 0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 3), 2)
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)
        self.assertEqual(self.calc.divide(0, 1), 0)
    def test_divide_negative(self):
        self.assertEqual(self.calc.divide(-6, 3), -2)
        self.assertEqual(self.calc.divide(6, -3), -2)
        self.assertEqual(self.calc.divide(-6, -3), 2)
    def test_divide_float(self):
        self.assertAlmostEqual(self.calc.divide(5.0, 2.0), 2.5)
        self.assertAlmostEqual(self.calc.divide(7.5, 2.5), 3.0)
        self.assertAlmostEqual(self.calc.divide(0.1, 0.2), 0.5)
    def test_divide_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(0, 0)
        with self.assertRaises(ValueError):
            self.calc.divide(0, -1)
        with self.assertRaises(ValueError):
            self.calc.divide(0, 1)
    def test_divide_large_numbers(self):
        self.assertEqual(self.calc.divide(1000000, 1000), 1000)
        self.assertEqual(self.calc.divide(1000000, 2000), 500)
        self.assertEqual(self.calc.divide(1000000, -1000), -1000)
    def test_divide_small_numbers(self):
        self.assertAlmostEqual(self.calc.divide(0.0001, 0.0001), 1)
        self.assertAlmostEqual(self.calc.divide(0.0001, 0.0002), 0.5)
        self.assertAlmostEqual(self.calc.divide(0.0001, -0.0001), -1)


if __name__ == '__main__':
    unittest.main()
