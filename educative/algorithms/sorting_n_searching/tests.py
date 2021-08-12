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

    # Challenge 2: Search in a Rotated List
    def test_pivoted_binary_search(self):
        lst = [7, 8, 9, 0, 3, 5, 6]
        self.assertEqual(4, pivoted_binary_search(lst, 7, 3))

    # Challenge 3: Group Anagrams
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

    # Challenge 4: Arrange a Binary List
    def test_sort_binary_list(self):
        lst = [1, 0, 1, 0, 1, 1, 0, 0]
        self.assertEqual(sorted(lst), sort_binary_list(lst))

    # Challenge 5: Find the Maximum Product of Two Integers in a List
    def test_find_max_prod(self):
        lst = [1, 3, 5, 2, 6]
        self.assertEqual([5, 6], find_max_prod(lst))

        lst = [1, 2, 3, 4, 5, 6, 7, 8]
        self.assertEqual([7, 8], find_max_prod(lst))

        lst = [0, 1, 0, 1, 0, 1]
        self.assertEqual([1, 1], find_max_prod(lst))

        lst = [1, -3, -5, 2, 6]
        self.assertEqual([-3, -5], find_max_prod(lst))
