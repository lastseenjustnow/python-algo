from LinkedList import *
from Node import Node
import random

import unittest


class TestLinkedListSolution(unittest.TestCase):

    def test_challenge_1(self):
        n = Node(0)
        n.next_element = Node(1)
        n.next_element.next_element = Node(2)
        lst = LinkedList()
        lst.head_node = n

        lst.insert_at_tail(3)
        self.assertTrue(lst.print_list())

    def test_challenge_2(self):
        lst = LinkedList().from_list([5, 90, 10, 4])
        self.assertTrue(lst.search(4))
        self.assertFalse(lst.search(6))

    def test_challenge_3(self):
        lst = LinkedList().from_list([3, 2, 1, 0])
        self.assertTrue(lst.search(2))
        lst.delete(2)
        self.assertFalse(lst.search(2))

        l2 = LinkedList().from_list([3, 2, 1, 0])
        self.assertTrue(l2.search(0))
        l2.delete(0)
        self.assertFalse(l2.search(0))

        l3 = LinkedList().from_list([3, 2, 1, 0])
        self.assertTrue(l3.search(3))
        l2.delete(3)
        self.assertFalse(l2.search(3))

        l4 = LinkedList().from_list([3, 2, 1, 3, 0])
        self.assertTrue(l4.search(3))
        l2.delete(3)
        self.assertFalse(l2.search(3))

        l5 = LinkedList().from_list([4, 2, 1, 4, 0])
        self.assertFalse(l5.search(3))
        l2.delete(3)
        self.assertFalse(l2.search(3))

        l6 = LinkedList()
        self.assertFalse(l6.search(3))
        l2.delete(3)
        self.assertFalse(l2.search(3))

    def test_challenge_4(self):
        lst = LinkedList().from_list([3, 2, 1, 0])
        self.assertEqual(lst.length(), 4)

    def test_challenge_5(self):
        lst = LinkedList().from_list([4, 2, 1, 4, 0])
        rev_l = lst.reverse()
        self.assertEqual(rev_l.get_head().data, 0)

    def test_challenge_6(self):
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

        self.assertTrue(lst.detect_loop())

        lst = LinkedList().from_list([4, 2, 1, 4, 0])
        self.assertFalse(lst.detect_loop())

    def test_challenge_7(self):
        lst = LinkedList().from_list([4, 2, 1, 6, 0])
        self.assertEqual(lst.find_mid(), 1)

    def test_challenge_8(self):
        lst = LinkedList().from_list([7, 7, 7, 22, 14, 21, 14, 7])
        lst.remove_duplicates()
        self.assertEqual(4, lst.length())

    def test_challenge_9(self):
        lst1 = LinkedList().from_list([10, 20, 80, 60])
        lst2 = LinkedList().from_list([15, 20, 30, 60, 45])

        lst_union = union(lst1, lst2)
        lst_expected_1 = LinkedList().from_list([10, 20, 80, 60, 15, 30, 45])
        self.assertEqual(lst_union, lst_expected_1)

        lst_intersect = intersection(lst1, lst2)
        lst_expected_2 = LinkedList().from_list([20, 60])
        self.assertEqual(lst_intersect, lst_expected_2)

    def test_challenge_10(self):
        lst = [7, 14, 21, 14, 22, 7]
        linked_lst = LinkedList().from_list(lst)
        for i in range(1, linked_lst.length()):
            self.assertEqual(lst[-i], linked_lst.find_nth(i))

    def test_find_happy_number(self):
        self.assertTrue(find_happy_number(23))
        self.assertFalse(find_happy_number(12))

    def test_reverse_every_k_elements(self):

        def reverse_every_k_elements_list(lst, k):
            return [el for lst in [lst[i:i + k][::-1] for i in range(0, len(lst), k)] for el in lst]

        def reverse_every_k_range_test(list_length, k):
            lst = [a for a in range(1, list_length)]
            linked_lst = LinkedList().from_list(lst)
            head_linked_lst_1 = linked_lst.get_head()
            function_output = reverse_every_k_elements(head_linked_lst_1, k)
            expected_result = reverse_every_k_elements_list(lst, k)
            return function_output.to_list() == expected_result

        for _ in range(0, 100):
            length = random.randint(2, 100)
            rand_k = random.randint(1, length - 1)
            self.assertTrue(reverse_every_k_range_test(length, rand_k))

    def test_rotate_list(self):

        def rotate_unlinked_list(lst, n):
            leng = len(lst)
            rot_k = n - int(n / leng) * leng + (leng if n < 0 else 0)
            return lst[-rot_k:] + lst[:-rot_k]

        def rotate_list_test(list_length, k):
            lst = [a for a in range(1, list_length + 1)]
            linked_lst = LinkedList().from_list(lst)
            head_linked_lst = linked_lst.get_head()
            function_output = rotate_list(head_linked_lst, k)
            expected_result = rotate_unlinked_list(lst, k)
            return function_output.to_list() == expected_result

        for _ in range(0, 100):
            length = random.randint(2, 100)
            rand_k = random.randint(1, length - 1)
            self.assertTrue(rotate_list_test(length, rand_k))

    def test_add_integers(self):
        def reverse_int(x):
            return list(map(int, str(x)[::-1]))

        def add_integers_test(int1, int2):
            integer1 = LinkedList().from_list(reverse_int(int1))
            integer2 = LinkedList().from_list(reverse_int(int2))
            function_output = add_integers(integer1, integer2)
            function_result = function_output.to_list()
            expected_result = reverse_int(int1 + int2)
            return function_result == expected_result

        for _ in range(0, 10000):
            length = random.randint(0, 1000000)
            rand_k = random.randint(0, 1000000)
            self.assertTrue(add_integers_test(length, rand_k))

    def test_merge_lists(self):
        lists = [LinkedList().from_list(x) for x in [[2, 6, 8], [3, 6, 7], [1, 3, 4]]]
        heads = [l.get_head() for l in lists]
        function_output = merge_lists(heads).to_list()
        expected_result = [1, 2, 3, 3, 4, 6, 6, 7, 8]
        self.assertEqual(expected_result, function_output)

        lists_2 = [LinkedList().from_list(x) for x in [[5, 8, 9], [1, 7]]]
        heads_2 = [l.get_head() for l in lists_2]
        function_output_2 = merge_lists(heads_2).to_list()
        expected_result_2 = [1, 5, 7, 8, 9]
        self.assertEqual(expected_result_2, function_output_2)

