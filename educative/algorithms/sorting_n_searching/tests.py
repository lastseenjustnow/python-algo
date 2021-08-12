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

    # Challenge 6: Find Duplicates in a List with No Repetition
    def test_find_duplicates(self):
        lst = [1, 3, 1, 3, 5, 1, 4, 7, 7]
        self.assertEqual([1, 3, 7], find_duplicates(lst))

        lst = [1, 1, 2, 2, 5, 1, 5, 6]
        self.assertEqual([1, 2, 5], find_duplicates(lst))

        lst = [0, 1, 2, 3, 4, 5, 6]
        self.assertEqual([], find_duplicates(lst))

    # Challenge 7: Search in a 2D List
    def test_find_in(self):
        list = [[10, 11, 12, 13],
                [14, 15, 16, 17],
                [27, 29, 30, 31],
                [32, 33, 39, 50]]

        self.assertTrue(find_in(list, 30))
        self.assertFalse(find_in(list, 34))

        list = [[10, 11, 12, 13],
                [14, 15, 16, 17],
                [27, 29, 30, 31],
                [32, 33, 39, 80]]

        self.assertTrue(find_in(list, 10))
        self.assertFalse(find_in(list, 35))
        self.assertFalse(find_in(list, 48))
        self.assertTrue(find_in(list, 80))
        self.assertTrue(find_in(list, 11))
        self.assertFalse(find_in(list, 0))
        self.assertTrue(find_in(list, 32))
        self.assertFalse(find_in(list, 22))

    # Challenge 9: Dutch National Flag Problem
    def test_dutch_national_flag(self):
        lst = [2, 0, 0, 1, 2, 1, 0]
        result = [0, 0, 0, 1, 1, 2, 2]
        self.assertEqual(result, dutch_national_flag(lst))

        lst = [2, 0, 0, 1, 2, 1]
        result = [0, 0, 1, 1, 2, 2]
        self.assertEqual(result, dutch_national_flag(lst))

        lst = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 1]
        result = [0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2]
        self.assertEqual(result, dutch_national_flag(lst))

    # Search in a Sorted Infinite Array
    def test_search_in_infinite_array(self):
        reader = ArrayReader([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])
        self.assertEqual(6, search_in_infinite_array(reader, 16))
        self.assertEqual(-1, search_in_infinite_array(reader, 11))

        reader = ArrayReader([1, 3, 8, 10, 15])
        self.assertEqual(4, search_in_infinite_array(reader, 15))
        self.assertEqual(-1, search_in_infinite_array(reader, 200))
