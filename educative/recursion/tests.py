import unittest

from solutions import *


class TestRecursion(unittest.TestCase):

    # Challenge 1: Find the Greatest Common Divisor
    def test_gcd(self):
        self.assertEqual(7, gcd(21, 35))

    # Challenge 2: Pascal's Triangle
    def test_printPascal(self):
        self.assertEqual([1, 2, 1], printPascal(2))
        self.assertEqual([1, 5, 10, 10, 5, 1], printPascal(5))

    # Challenge 3: Convert Decimal Number to Binary Number
    def test_decimalToBinary(self):
        self.assertEqual('1011', decimalToBinary(11))
        self.assertEqual('0', decimalToBinary(0))
        self.assertEqual('10', decimalToBinary(2))

    # Challenge 2: Balance Parenthesis
    def test_balanced(self):
        testVariable = ["(", ")", "(", ")"]
        self.assertTrue(balanced(testVariable, 0, 0))
