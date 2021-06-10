import unittest

from solutions import *


class TestHashTableSolution(unittest.TestCase):

    def test_challenge_1(self):
        list1 = [9, 4, 7, 1, -2, 6, 5]
        list2 = [7, 1, -2]
        self.assertTrue(is_subset(list1, list2))

    def test_challenge_2(self):
        list1 = [9, 4, 3, 1, -2, 6, 5]
        list2 = [7, 10, 8]
        self.assertTrue(is_disjoint(list1, list2))
