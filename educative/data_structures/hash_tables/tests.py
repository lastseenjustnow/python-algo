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

    def test_challenge_5(self):
        lst = [3, 4, 7, 1, 12, 9]
        expected_result = [[4, 12], [7, 9]]
        function_output = find_pair(lst)
        self.assertTrue(expected_result, function_output)

    def test_challenge_6(self):
        my_list = [6, 4, -7, 3, 12, 9]
        self.assertTrue(find_sub_zero(my_list))

    def test_challenge_7(self):
        lst = ["the", "hello", "there", "answer", "any",
               "by", "world", "their", "abc"]

        word = "helloworld"
        self.assertTrue(is_formation_possible(lst, word))

    def test_challenge_8(self):
        lst = [1, 21, 3, 14, 5, 60, 7, 6]
        k = 81
        function_output = findSum(lst, k)
        expected_result = [60, 21]
        self.assertEqual(expected_result, function_output)

    def test_challenge_9(self):
        lst = [9, 2, 3, 2, 6, 6]
        function_output = findFirstUnique(lst)
        self.assertEqual(9, function_output)

        lst = [4, 5, 1, 2, 0, 4]
        function_output = findFirstUnique(lst)
        self.assertEqual(5, function_output)

    def test_challenge_10(self):
        lst = LinkedList()

        lst.insert_at_head(21)
        lst.insert_at_head(14)
        lst.insert_at_head(7)

        # Adding a loop
        head = lst.get_head()
        node = lst.get_head()

        for i in range(4):
            if node.next_element is None:
                node.next_element = head.next_element
                break
            node = node.next_element
        self.assertTrue(detect_loop(lst))

        lst = LinkedList().from_list([4, 2, 1, 4, 0])
        self.assertFalse(lst.detect_loop())

    def test_challenge_11(self):
        lst = LinkedList().from_list([7, 7, 7, 22, 14, 21, 14, 7])
        remove_duplicates(lst)
        lst.print_list()
        self.assertEqual(4, lst.length())

    def test_challenge_12(self):
        lst1 = LinkedList().from_list([10, 20, 80, 60])
        lst2 = LinkedList().from_list([15, 20, 30, 60, 45])

        lst_union = union(lst1, lst2)
        lst_expected_1 = LinkedList().from_list([10, 20, 80, 60, 15, 30, 45])
        self.assertEqual(lst_union, lst_expected_1)

        lst1 = LinkedList().from_list([10, 20, 80, 60])
        lst2 = LinkedList().from_list([15, 20, 30, 60, 45])
        lst_intersect = intersection(lst1, lst2)
        lst_expected_2 = LinkedList().from_list([20, 60])
        self.assertEqual(lst_intersect, lst_expected_2)
