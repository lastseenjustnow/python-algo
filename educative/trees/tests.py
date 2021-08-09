import unittest
import random

from BinaryTreeNode import create_BST
from educative.trees.InorderIterator import InorderIterator
from solutions import *


class TestStackSolution(unittest.TestCase):

    # Check if Two Binary Trees are Identical
    def test_are_identical(self):
        lst = [25, 50, 75, 100, 125, 200, 300]
        tree1 = create_BST(lst)

        tree2 = BinaryTreeNode(100)
        tree2.left = BinaryTreeNode(50)
        tree2.left.left = BinaryTreeNode(25)
        tree2.left.right = BinaryTreeNode(75)
        tree2.right = BinaryTreeNode(200)
        tree2.right.left = BinaryTreeNode(125)
        tree2.right.right = BinaryTreeNode(300)

        self.assertTrue(are_identical(tree1, tree2))

        lst1 = [25, 50, 75, 100, 125, 200, 350]
        lst2 = [25, 50, 75, 100, 125, 200, 355]
        tree1 = create_BST(lst1)
        tree2 = create_BST(lst2)

        self.assertFalse(are_identical(tree1, tree2))

        tree1 = BinaryTreeNode(100)
        tree1.left = BinaryTreeNode(50)
        tree1.left.left = BinaryTreeNode(25)
        tree1.right = BinaryTreeNode(200)
        tree1.right.left = BinaryTreeNode(125)
        tree1.right.right = BinaryTreeNode(350)

        tree2 = BinaryTreeNode(100)
        tree2.left = BinaryTreeNode(50)
        tree2.left.right = BinaryTreeNode(25)
        tree2.right = BinaryTreeNode(200)
        tree2.right.left = BinaryTreeNode(125)
        tree2.right.right = BinaryTreeNode(350)

        self.assertFalse(are_identical(tree1, tree2))

    # In-Order Iterator for a Binary Tree
    def test_inorder_using_iterator(self):
        arr = sorted([25, 125, 200, 300, 75, 50, 12, 35, 60, 75])
        root = create_BST(arr)
        expected_result = "12 25 35 50 60 75 75 125 200 300 "
        function_result = InorderIterator(root).inorder_using_iterator()
        self.assertEqual(expected_result, function_result)

    def test_inorder_successor_bst(self):
        arr = sorted(list(set([random.randint(-1000, 1000) for _ in range(random.randint(0, 100000))])))
        root = create_BST(arr)
        for i, el in enumerate(arr[:-1], 0):
            self.assertEqual(arr[i+1], inorder_successor_bst(root, el))

    # In-order Successor Binary Search Tree With Parent Pointers
    def test_find_successor_with_parent_pointers(self):
        tree = BinaryTreeNode(100)
        tree.left = BinaryTreeNode(50)
        tree.left.next = tree
        tree.left.left = BinaryTreeNode(25)
        tree.left.right = BinaryTreeNode(75)
        tree.left.left.next = tree.left.right.next = tree.left
        tree.right = BinaryTreeNode(200)
        tree.right.next = tree
        tree.right.left = BinaryTreeNode(125)
        tree.right.right = BinaryTreeNode(350)
        tree.right.left.next = tree.right.right.next = tree.right

        self.assertEqual(100, find_successor_with_parent_pointers(tree, 75).data)
        self.assertEqual(125, find_successor_with_parent_pointers(tree, 100).data)
        self.assertEqual(350, find_successor_with_parent_pointers(tree, 200).data)

    def test_level_order_traversal(self):
        root = BinaryTreeNode(100)
        root.left = BinaryTreeNode(50)
        root.left.left = BinaryTreeNode(25)
        root.left.right = BinaryTreeNode(75)
        root.right = BinaryTreeNode(200)
        root.right.right = BinaryTreeNode(350)

        function_res = level_order_traversal(root)
        expected_res = "100\n50 200\n25 75 350"
        self.assertEqual(expected_res, function_res)

    def test_traverse(self):
        root = BinaryTreeNode(12)
        root.left = BinaryTreeNode(7)
        root.right = BinaryTreeNode(1)
        root.left.left = BinaryTreeNode(9)
        root.right.left = BinaryTreeNode(10)
        root.right.right = BinaryTreeNode(5)

        function_res = traverse(root)
        expected_res = deque([[9, 10, 5], [7, 1], [12]])

        self.assertEqual(expected_res, function_res)

    def test_find_level_averages(self):
        root = BinaryTreeNode(12)
        root.left = BinaryTreeNode(7)
        root.right = BinaryTreeNode(1)
        root.left.left = BinaryTreeNode(9)
        root.left.right = BinaryTreeNode(2)
        root.right.left = BinaryTreeNode(10)
        root.right.right = BinaryTreeNode(5)

        function_res = find_level_averages(root)
        expected_res = [12.0, 4.0, 6.5]

        self.assertEqual(expected_res, function_res)

    def test_find_successor(self):
        root = BinaryTreeNode(12)
        root.left = BinaryTreeNode(7)
        root.right = BinaryTreeNode(1)
        root.left.left = BinaryTreeNode(9)
        root.right.left = BinaryTreeNode(10)
        root.right.right = BinaryTreeNode(5)

        self.assertEqual(7, find_successor(root, 12))
        self.assertEqual(10, find_successor(root, 9))

    def test_zigzag_traverse(self):
        root = BinaryTreeNode(1)
        root.left = BinaryTreeNode(2)
        root.right = BinaryTreeNode(3)
        root.left.left = BinaryTreeNode(4)
        root.left.right = BinaryTreeNode(5)
        root.right.left = BinaryTreeNode(6)
        root.right.right = BinaryTreeNode(7)

        expected_res = [[1], [3, 2], [4, 5, 6, 7]]
        function_res = zigzag_traverse(root)

        self.assertEqual(expected_res, function_res)

        root = BinaryTreeNode(12)
        root.left = BinaryTreeNode(7)
        root.right = BinaryTreeNode(1)
        root.left.left = BinaryTreeNode(9)
        root.right.left = BinaryTreeNode(10)
        root.right.right = BinaryTreeNode(5)
        root.right.left.left = BinaryTreeNode(20)
        root.right.left.right = BinaryTreeNode(17)

        expected_res = [[12], [1, 7], [9, 10, 5], [17, 20]]
        function_res = zigzag_traverse(root)

        self.assertEqual(expected_res, function_res)

    def test_connect_level_order_siblings(self):
        root = BinaryTreeNode(1)
        root.left = BinaryTreeNode(2)
        root.right = BinaryTreeNode(3)
        root.left.left = BinaryTreeNode(4)
        root.left.right = BinaryTreeNode(5)
        root.right.left = BinaryTreeNode(6)
        root.right.right = BinaryTreeNode(7)

        connect_level_order_siblings(root)
        self.assertIsNone(root.next)
        self.assertEqual(7, root.right.left.next.data)

    def test_is_bst(self):
        root = BinaryTreeNode(100)
        root.left = BinaryTreeNode(50)
        root.left.left = BinaryTreeNode(25)
        root.left.right = BinaryTreeNode(75)
        root.right = BinaryTreeNode(200)
        root.right.left = BinaryTreeNode(125)
        root.right.right = BinaryTreeNode(350)

        self.assertTrue(is_bst(root))

        root = BinaryTreeNode(100)
        root.left = BinaryTreeNode(50)
        root.left.left = BinaryTreeNode(25)
        root.left.right = BinaryTreeNode(75)
        root.right = BinaryTreeNode(200)
        root.right.left = BinaryTreeNode(90)
        root.right.right = BinaryTreeNode(350)

        self.assertFalse(is_bst(root))

        root = BinaryTreeNode(100)
        root.left = BinaryTreeNode(50)
        root.left.left = BinaryTreeNode(25)
        root.left.right = BinaryTreeNode(110)
        root.right = BinaryTreeNode(200)
        root.right.left = BinaryTreeNode(150)
        root.right.right = BinaryTreeNode(350)

        self.assertFalse(is_bst(root))

    def test_convert_to_linked_list(self):
        root = BinaryTreeNode(100)
        root.left = BinaryTreeNode(50)
        root.right = BinaryTreeNode(200)
        root.left.left = BinaryTreeNode(25)
        root.left.right = BinaryTreeNode(75)
        root.left.left.right = BinaryTreeNode(30)
        root.left.right.left = BinaryTreeNode(60)
        root.left.right.left.left = BinaryTreeNode(55)
        root.right.left = BinaryTreeNode(125)
        root.right.right = BinaryTreeNode(350)

        res_root = convert_to_linked_list(root)
        expected_results = [25, 30, 50, 55, 60, 75, 100, 125, 200, 350]

        for result in expected_results:
            self.assertEqual(result, res_root.data)
            res_root = res_root.right

    def test_display_tree_perimeter(self):
        root = BinaryTreeNode(100)
        root.left = BinaryTreeNode(50)
        root.right = BinaryTreeNode(200)
        root.left.left = BinaryTreeNode(25)
        root.left.left.left = BinaryTreeNode(10)
        root.left.right = BinaryTreeNode(60)
        root.left.right.right = BinaryTreeNode(70)
        root.right = BinaryTreeNode(200)
        root.right.right = BinaryTreeNode(350)
        root.right.right.right = BinaryTreeNode(400)

        expected_result = '100 50 25 10 70 400 350 200 '

        self.assertEqual(expected_result, display_tree_perimeter(root))

    def test_populate_sibling_pointers(self):
        root = BinaryTreeNode(100)
        root.left = BinaryTreeNode(50)
        root.right = BinaryTreeNode(200)
        root.left.left = BinaryTreeNode(25)
        root.left.right = BinaryTreeNode(75)
        root.right.right = BinaryTreeNode(300)
        root.right.right.right = BinaryTreeNode(350)

        expected_results = [100, 50, 200, 25, 75, 300, 350]
        populate_sibling_pointers(root)
        for result in expected_results:
            self.assertEqual(result, root.data)
            root = root.right

    def test_serializer(self):
        arr = [100, 50, 200, 25, 75, 125, 350]
        root = create_BST(arr)
        output = open('data.class', 'wb')
        p = pickle.Pickler(output)
        serialize(root, p)
        output.close()
        input2 = open('data.class', 'rb')
        root_deserialized = deserialize(input2)
        self.assertEqual(25, root_deserialized.data)
        input2.close()

    def test_find_nth_highest_in_bst(self):
        arr = [25, 50, 75, 100, 125, 200, 350]
        bst = create_BST(arr)
        for i, el in enumerate(arr[::-1]):
            self.assertEqual(el, find_nth_highest_in_bst(bst, i + 1).data)

    def test_mirror_tree(self):
        def test(f: Callable):
            root = BinaryTreeNode(20)
            root.left = BinaryTreeNode(50)
            root.right = BinaryTreeNode(200)
            root.left.left = BinaryTreeNode(75)
            root.left.right = BinaryTreeNode(25)
            root.right.right = BinaryTreeNode(300)

            mirror_root = f(root)

            self.assertEqual(200, mirror_root.left.data)
            self.assertIsNone(mirror_root.left.right)
            self.assertEqual(50, mirror_root.right.data)
            self.assertEqual(300, mirror_root.left.left.data)
            self.assertEqual(25, mirror_root.right.left.data)
            self.assertEqual(75, mirror_root.right.right.data)

        test(mirror_tree)
        test(mirror_tree_rec)

    def test_delete_zero_sum_subtree(self):
        root = BinaryTreeNode(7)
        root.left = BinaryTreeNode(5)
        root.right = BinaryTreeNode(6)
        root.left.left = BinaryTreeNode(-3)
        root.left.right = BinaryTreeNode(-2)

        new_root = delete_zero_sum_subtree(root)
        self.assertIsNone(new_root.left)

    # Convert N-ary Tree to Binary Tree
    def test_convert_n_ary_to_binary(self):
        nary_root = NaryTreeNode(1)
        nary_root.children.append(NaryTreeNode(2))
        nary_root.children.append(NaryTreeNode(3))
        nary_root.children.append(NaryTreeNode(4))
        nary_root.children[1].children.append(NaryTreeNode(5))
        nary_root.children[1].children.append(NaryTreeNode(6))

        function_output = convert_n_ary_to_binary(nary_root)
        self.assertEqual(1, function_output.data)
        self.assertEqual(2, function_output.left.data)
        self.assertEqual(3, function_output.left.left.data)
        self.assertEqual(4, function_output.left.left.left.data)
        self.assertEqual(5, function_output.left.left.right.data)
        self.assertEqual(6, function_output.left.left.right.right.data)

    # Minimum Depth of a Binary Tree
    def test_find_minimum_depth(self):
        # Example 1
        root = BinaryTreeNode(1)
        root.left = BinaryTreeNode(2)
        root.right = BinaryTreeNode(3)
        root.left.left = BinaryTreeNode(4)
        root.left.right = BinaryTreeNode(5)
        self.assertEqual(2, find_minimum_depth(root))

        # Example 2
        root = BinaryTreeNode(12)
        root.left = BinaryTreeNode(7)
        root.right = BinaryTreeNode(1)
        root.right.left = BinaryTreeNode(10)
        root.right.right = BinaryTreeNode(5)
        self.assertEqual(2, find_minimum_depth(root))

        # Example 3
        root = BinaryTreeNode(12)
        root.left = BinaryTreeNode(7)
        root.left.left = BinaryTreeNode(9)
        root.right = BinaryTreeNode(1)
        root.right.left = BinaryTreeNode(10)
        root.right.right = BinaryTreeNode(5)
        root.right.left.left = BinaryTreeNode(11)
        self.assertEqual(3, find_minimum_depth(root))

    def test_find_paths(self):
        # Example 1
        root = BinaryTreeNode(1)
        root.left = BinaryTreeNode(7)
        root.right = BinaryTreeNode(9)
        root.left.left = BinaryTreeNode(4)
        root.left.right = BinaryTreeNode(5)
        root.right.left = BinaryTreeNode(2)
        root.right.right = BinaryTreeNode(7)
        self.assertEqual([[1, 7, 4], [1, 9, 2]], find_paths(root, 12))

        # Example 2
        root = BinaryTreeNode(12)
        root.left = BinaryTreeNode(7)
        root.right = BinaryTreeNode(1)
        root.left.left = BinaryTreeNode(4)
        root.right.left = BinaryTreeNode(10)
        root.right.right = BinaryTreeNode(5)
        self.assertEqual([[12, 7, 4], [12, 1, 10]], find_paths(root, 23))

    def test_find_sum_of_path_numbers(self):
        # Example 1
        root = BinaryTreeNode(1)
        root.left = BinaryTreeNode(7)
        root.right = BinaryTreeNode(9)
        root.right.left = BinaryTreeNode(2)
        root.right.right = BinaryTreeNode(9)
        self.assertEqual(408, find_sum_of_path_numbers(root))

        # Example 2
        root = BinaryTreeNode(1)
        root.left = BinaryTreeNode(0)
        root.right = BinaryTreeNode(1)
        root.left.left = BinaryTreeNode(1)
        root.right.left = BinaryTreeNode(6)
        root.right.right = BinaryTreeNode(5)
        self.assertEqual(332, find_sum_of_path_numbers(root))

    def test_find_path(self):

        root = BinaryTreeNode(1)
        root.left = BinaryTreeNode(0)
        root.right = BinaryTreeNode(1)
        root.left.left = BinaryTreeNode(1)
        root.right.left = BinaryTreeNode(6)
        root.right.right = BinaryTreeNode(5)

        self.assertFalse(find_path(root, [1, 0, 7]))
        self.assertTrue(find_path(root, [1, 1, 6]))

    def test_count_paths(self):
        # Example 1
        root = BinaryTreeNode(1)
        root.left = BinaryTreeNode(7)
        root.left.left = BinaryTreeNode(6)
        root.left.right = BinaryTreeNode(5)
        root.right = BinaryTreeNode(9)
        root.right.left = BinaryTreeNode(2)
        root.right.right = BinaryTreeNode(3)
        self.assertEqual(3, count_paths(root, 12))

        # Example 2
        root = BinaryTreeNode(12)
        root.left = BinaryTreeNode(7)
        root.right = BinaryTreeNode(1)
        root.left.left = BinaryTreeNode(4)
        root.right.left = BinaryTreeNode(10)
        root.right.right = BinaryTreeNode(5)
        self.assertEqual(2, count_paths(root, 11))

    def test_find_median(self):
        medianOfAStream = MedianOfAStream()
        medianOfAStream.insert_num(3)
        medianOfAStream.insert_num(1)
        self.assertEqual(2, medianOfAStream.find_median())
        medianOfAStream.insert_num(5)
        self.assertEqual(3, medianOfAStream.find_median())
        medianOfAStream.insert_num(4)
        self.assertEqual(3.5, medianOfAStream.find_median())

    def test_find_sliding_window_median(self):
        slidingWindowMedian_1 = SlidingWindowMedian()
        result_1 = slidingWindowMedian_1.find_sliding_window_median([1, 2, -1, 3, 5], 2)
        self.assertEqual([1.5, 0.5, 1.0, 4.0], result_1)

        slidingWindowMedian_2 = SlidingWindowMedian()
        result_2 = slidingWindowMedian_2.find_sliding_window_median([1, 2, -1, 3, 5], 3)
        self.assertEqual([1.0, 2.0, 3.0], result_2)

    def test_find_maximum_capital(self):
        self.assertEqual(6, find_maximum_capital([0, 1, 2], [1, 2, 3], 2, 1))
        self.assertEqual(8, find_maximum_capital([0, 1, 2, 3], [1, 2, 3, 5], 3, 0))