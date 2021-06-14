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

    def test_challenge_3(self):
        list1 = [[1, 2], [3, 4], [5, 9], [4, 3], [9, 5]]
        expected_result = [[3, 4], [5, 9], [4, 3], [9, 5]]
        function_output = find_symmetric(list1)
        self.assertTrue(expected_result, function_output)

    def test_challenge_4(self):
        dct = {
            "NewYork": "Chicago",
            "Boston": "Texas",
            "Missouri": "NewYork",
            "Texas": "Missouri"
        }
        function_output = trace_path(dct)
        expected_result = [['Boston', 'Texas'],
                           ['Texas', 'Missouri'],
                           ['Missouri', 'NewYork'],
                           ['NewYork', 'Chicago']]
        self.assertTrue(expected_result, function_output)

