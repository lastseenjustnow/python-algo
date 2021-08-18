import unittest

from solutions import *

profit_1 = [60, 100, 120]
profits_length_1 = 3
weight_1 = [10, 20, 30]
capacity_1 = 50

profit_2 = [1, 2, 2, 4, 10]
profits_length_2 = 5
weight_2 = [1, 1, 2, 12, 4]
capacity_2 = 15


class TestGraphAlgorithmsSolution(unittest.TestCase):

    # Challenge 1: The 0/1 Knapsack Problem
    def test_knap_sack_brute_force_iterative(self):
        self.assertEqual(220, knap_sack_brute_force_iterative(profit_1, profits_length_1, weight_1, capacity_1))
        self.assertEqual(15, knap_sack_brute_force_iterative(profit_2, profits_length_2, weight_2, capacity_2))

    def test_knap_sack_brute_force_recursive(self):
        self.assertEqual(220, knap_sack_brute_force_recursive(profit_1, profits_length_1, weight_1, capacity_1))
        self.assertEqual(15, knap_sack_brute_force_recursive(profit_2, profits_length_2, weight_2, capacity_2))

    def test_knap_sack_memoization(self):
        self.assertEqual(220, knap_sack_memoization(profit_1, profits_length_1, weight_1, capacity_1))
        self.assertEqual(15, knap_sack_memoization(profit_2, profits_length_2, weight_2, capacity_2))

    def test_knap_sack_tabularization(self):
        self.assertEqual(220, knap_sack_tabularization(profit_1, profits_length_1, weight_1, capacity_1))
        self.assertEqual(15, knap_sack_tabularization(profit_2, profits_length_2, weight_2, capacity_2))

    def test_knap_sack_tabularization_optimized(self):
        self.assertEqual(220, knap_sack_tabularization_optimized(profit_1, profits_length_1, weight_1, capacity_1))
        self.assertEqual(15, knap_sack_tabularization_optimized(profit_2, profits_length_2, weight_2, capacity_2))
