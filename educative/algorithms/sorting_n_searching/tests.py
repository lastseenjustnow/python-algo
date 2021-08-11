import unittest

from solutions import *


class TestArraySolution(unittest.TestCase):

    # Challenge 1: Find Two Numbers that Add up to "n"
    def test_find_sum(self):
        lst = [1, 21, 3, 14, 5, 60, 7, 6]
        n = 81

        self.assertEqual((21, 60), find_sum_brute_force(lst, n))
        self.assertEqual((21, 60), find_sum_sorting(lst, n))
        self.assertEqual((21, 60), find_sum_dictionary(lst, n))
        self.assertEqual((21, 60), find_sum_set(lst, n))

    def test_pivoted_binary_search(self):
        lst = [7, 8, 9, 0, 3, 5, 6]
        self.assertEqual(4, pivoted_binary_search(lst, 7, 3))

    def test_anagrams(self):
        input = [
            'tom marvolo riddle ',
            'abc',
            'def',
            'cab',
            'fed',
            'brag',
            'clint eastwood ',
            'i am lord voldemort',
            'elvis',
            'grab',
            'old west action',
            'lives'
        ]
        expected_result = [['abc', 'cab'], ['def', 'fed'], ['tom marvolo riddle ', 'i am lord voldemort'], ['brag', 'grab'], ['clint eastwood ', 'old west action'], ['elvis', 'lives']]
        self.assertEqual(expected_result, anagrams(input))
