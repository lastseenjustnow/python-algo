import unittest

from solutions import *


class TestGreedyAlgorithmSolution(unittest.TestCase):
    # Challenge 1: Counting Money!
    def test_find_min_coins(self):
        available_coins = [1, 5, 10, 25]
        self.assertEqual([10, 5, 1, 1, 1, 1], find_min_coins(19, available_coins))

    # Challenge 2: Connecting n Pipes with Minimum Cost
    def test_min_cost(self):
        self.assertEqual(29, min_cost([4, 3, 2, 6]))
        self.assertEqual(16, min_cost([1, 1, 2, 6]))

    # Challenge 3: Find the Egyptian Fraction's Denominators
    def test_egyptian_fraction(self):
        self.assertEqual([2, 6], egyptian_fraction(2, 3))
        self.assertEqual([2, 8], egyptian_fraction(5, 8))
        self.assertEqual([3, 11, 231], egyptian_fraction(6, 14))
