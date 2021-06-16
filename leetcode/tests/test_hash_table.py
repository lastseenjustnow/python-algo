import unittest

from leetcode.solutions.hash_table import *


class TestHashTableSolution(unittest.TestCase):

    def test_LRUCache_implementation(self):
        with self.assertRaises(ValueError):
            LRUCache(-1)

    def test_LRUCache_methods_1(self):
        lRUCache = LRUCache(2)
        lRUCache.put(1, 1)
        self.assertEqual(OrderedDict([(1, 1)]), lRUCache.cache)

        lRUCache.put(2, 2)
        self.assertEqual(OrderedDict([(1, 1), (2, 2)]), lRUCache.cache)

        self.assertEqual(1, lRUCache.get(1))
        lRUCache.put(3, 3)
        self.assertEqual(OrderedDict([(1, 1), (3, 3)]), lRUCache.cache)
        self.assertEqual(-1, lRUCache.get(2))

        lRUCache.put(4, 4)
        # self.assertEqual(OrderedDict([(4, 4), (3, 3)]), lRUCache.cache) # contradiction with logic at line 18
        self.assertEqual(-1, lRUCache.get(1))
        self.assertEqual(3, lRUCache.get(3))
        self.assertEqual(4, lRUCache.get(4))

    def test_LRUCache_methods_2(self):
        lRUCache = LRUCache(2)
        lRUCache.put(2, 1)
        self.assertEqual(OrderedDict([(2, 1)]), lRUCache.cache)
        lRUCache.put(1, 1)
        self.assertEqual(OrderedDict([(2, 1), (1, 1)]), lRUCache.cache)
        lRUCache.put(2, 3)
        self.assertEqual(OrderedDict([(1, 1), (2, 3)]), lRUCache.cache)
        lRUCache.put(4, 1)
        self.assertEqual(-1, lRUCache.get(1))
        self.assertEqual(3, lRUCache.get(2))
        self.assertEqual(OrderedDict([(4, 1), (2, 3)]), lRUCache.cache)