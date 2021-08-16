import unittest

from solutions import *


class TestGreedyAlgorithmSolution(unittest.TestCase):
    def test_find_min_coins(self):
        available_coins = [1, 5, 10, 25]
        self.assertEqual([10, 5, 1, 1, 1, 1], find_min_coins(19, available_coins))
