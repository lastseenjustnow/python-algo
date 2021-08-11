import unittest

from solutions import *

keys = ["the", "a", "there", "answer", "any",
        "by", "bye", "their", "abc"]

t = Trie()

for words in keys:
    t.insert(words)


class TestTriesSolution(unittest.TestCase):

    # Challenge 1: Total Number of Words in a Trie
    def test_total_words(self):
        self.assertEqual(9, total_words(t.root))

    # Challenge 2: Find All Words Stored in Trie
    def test_find_words(self):
        expected_result = ["a", "abc", "answer", "any", "by", "bye", "the", "their", "there"]
        self.assertEqual(expected_result, find_words(t.root))

    # Challenge 3: List Sort Using Trie
    def test_sort_list(self):
        input_array = ["the", "a", "there", "answer", "any", "by", "bye", "their", "abc"]
        expected_result = ["a", "abc", "answer", "any", "by", "bye", "the", "their", "there"]
        self.assertEqual(sort_list(input_array), expected_result)

    # Challenge 4: Word Formation From a Dictionary Using Trie
    def test_is_formation_possible(self):
        dictionary = ['the', 'hello', 'there', 'answer', 'any', 'by', 'world', 'their', 'abc']
        self.assertTrue(is_formation_possible(dictionary, 'helloworld'))
        self.assertFalse(is_formation_possible(dictionary, 'helloworldd'))
        self.assertTrue(is_formation_possible(dictionary, 'byworld'))
        self.assertFalse(is_formation_possible(dictionary, 'byword'))
