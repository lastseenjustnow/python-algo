import unittest

from solutions import *


class TestGraphAlgorithmsSolution(unittest.TestCase):

    def test_knap_sack(self):
        profit = [60, 100, 120]
        profits_length = 3
        weight = [10, 20, 30]
        capacity = 50
        self.assertEqual(220, knap_sack(profit, profits_length, weight, capacity))

        profit = [1, 2, 2, 4, 10]
        profits_length = 5
        weight = [1, 1, 2, 12, 4]
        capacity = 15
        self.assertEqual(15, knap_sack(profit, profits_length, weight, capacity))
