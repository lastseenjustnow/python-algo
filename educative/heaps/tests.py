import unittest

from solutions import *


class TestHashTableSolution(unittest.TestCase):

    # Challenge 1: Convert Max-Heap to Min-Heap
    def test_convertMax(self):
        maxHeap = [9, 4, 7, 1, -2, 6, 5]
        expected_result = [-2, 1, 5, 4, 9, 6, 7]
        self.assertEqual(expected_result, convertMax(maxHeap))

        maxHeap = [16, 15, 14, 12, 4, 7, 9, 2, 3, 1]
        expected_result = [1, 2, 7, 3, 4, 14, 9, 15, 12, 16]
        self.assertEqual(expected_result, convertMax(maxHeap))

    # Challenge 2: Find k smallest elements in a List
    def test_findKSmallest(self):
        lst = [9, 4, 7, 1, -2, 6, 5]
        self.assertEqual([-2, 1], findKSmallest(lst, 2))
        lst = [9, 4, 7, 1, -2, 6, 5]
        self.assertEqual([-2, 1, 4], findKSmallest(lst, 3))
        lst = [9, 4, 7, 1, -2, 6, 5]
        self.assertEqual([-2, 1, 4, 5, 6], findKSmallest(lst, 5))

    # Challenge 3: Find k largest elements in the List
    def test_findKLargest(self):
        lst = [9, 4, 7, 1, -2, 6, 5]
        self.assertEqual([9, 7, 6], findKLargest(lst, 3))
