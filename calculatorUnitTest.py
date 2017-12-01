import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()
        print("SETUP IS RUN")

    def test_can_create_calculator_object(self):

        self.assertNotEqual(self.calculator, None)

    def test_can_add_numbers(self):

        self.assertEqual(6,self.calculator.add(4,2))

    def test_can_subtract_numbers(self):
        self.assertEqual(3,self.calculator.subtract(6,3))

    def test_can_time_numbers(self):
        self.assertEqual(10,self.calculator.time(2,5))

    def test_can_divide_numbers(self):
        self.assertEqual(5,self.calculator.divide(10,2))

unittest.main()
