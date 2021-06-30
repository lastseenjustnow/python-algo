from typing import Optional, List, Tuple, Deque
from collections import deque

from BinaryTreeNode import BinaryTreeNode


# Check if Two Binary Trees are Identical
def are_identical(root1: BinaryTreeNode, root2: BinaryTreeNode) -> bool:
    if root1 is None and root2 is not None:
        return False
    if root1 is not None and root2 is None:
        return False
    if root1 is None and root2 is None:
        return True

    return are_identical(root1.left, root2.left) \
        and are_identical(root1.right, root2.right)\
        and root1.data == root2.data


# In-order Successor of Binary Search Tree
def inorder_successor_bst(root: BinaryTreeNode, d: int) -> Optional[int]:
    potential_next = None
    while root.data != d:
        if d < root.data:
            potential_next = root.data
            root = root.left
        else:
            root = root.right

    if root.right:
        right_tree = root.right
        while right_tree:
            potential_next = right_tree.data
            right_tree = right_tree.left

    return potential_next


# Level Order Traversal of Binary Tree
def level_order_traversal(root: BinaryTreeNode) -> str:
    result = ""

    node_deque: Deque[BinaryTreeNode] = deque()
    level_deque: Deque[int] = deque()
    node_deque.append(root)
    current_level = 0
    level_deque.append(current_level)

    while len(node_deque) != 0:
        current_node = node_deque.popleft()
        current_node_level = level_deque.popleft()
        if current_node_level > current_level:
            result = result[:-1] + "\n"
            current_level = current_node_level
        result += str(current_node.data) + " "
        if current_node.left:
            node_deque.append(current_node.left)
            level_deque.append(current_level + 1)
        if current_node.right:
            node_deque.append(current_node.right)
            level_deque.append(current_level + 1)

    return result[:-1]


# Reverse Level Order Traversal (easy)
def traverse(root: BinaryTreeNode) -> Deque[List[int]]:
    result = deque()

    node_deque: Deque[BinaryTreeNode] = deque()
    level_deque: Deque[int] = deque()
    node_deque.append(root)
    current_level_values = []
    current_level = 0
    level_deque.append(current_level)

    while len(node_deque) != 0:
        current_node = node_deque.popleft()
        current_node_level = level_deque.popleft()
        if current_node_level > current_level:
            result.appendleft(current_level_values)
            current_level = current_node_level
            current_level_values = []
        current_level_values.append(current_node.data)
        if current_node.left:
            node_deque.append(current_node.left)
            level_deque.append(current_level + 1)
        if current_node.right:
            node_deque.append(current_node.right)
            level_deque.append(current_level + 1)

    result.appendleft(current_level_values)

    return result


# Level Averages in a Binary Tree (easy)
def find_level_averages(root):
    result: List[float] = []
    nodes_deque: Deque[Optional[BinaryTreeNode]] = deque()
    nodes_deque.append(root)
    nodes_deque.append(None)

    while len(nodes_deque) != 1:
        head = nodes_deque.popleft()
        sum = 0
        count = 0
        while head:
            sum += head.data
            count += 1
            if head.left:
                nodes_deque.append(head.left)
            if head.right:
                nodes_deque.append(head.right)
            head = nodes_deque.popleft()
        result.append(sum / count)
        nodes_deque.append(head)

    return result


# Level Order Successor (easy)
def find_successor(root, key):

    deq: Deque[Optional[BinaryTreeNode]] = deque()
    deq.append(root)
    is_key_found = False

    while deq:
        deq_len = len(deq)
        for _ in range(deq_len):
            if is_key_found:
                return deq.popleft().data
            current_node = deq.popleft()
            if current_node.data == key:
                is_key_found = True
            if current_node.left:
                deq.append(current_node.left)
            if current_node.right:
                deq.append(current_node.right)

    return None


# Zigzag Traversal (medium)
def zigzag_traverse(root):
    result = []

    deq: Deque[Optional[BinaryTreeNode]] = deque()
    deq.append(root)
    from_end = False

    while deq:
        len_deq = len(deq)
        current_level_values = []
        for _ in range(len_deq):
            if from_end:
                current_node = deq.pop()
                current_level_values.append(current_node.data)
                if current_node.right:
                    deq.appendleft(current_node.right)
                if current_node.left:
                    deq.appendleft(current_node.left)
            else:
                current_node = deq.popleft()
                current_level_values.append(current_node.data)
                if current_node.left:
                    deq.append(current_node.left)
                if current_node.right:
                    deq.append(current_node.right)
        result.append(current_level_values)
        from_end = not from_end

    return result


# Connect Level Order Siblings (medium)
def connect_level_order_siblings(root):

    deq: Deque[Optional[BinaryTreeNode]] = deque()
    deq.append(root)
    deq.append(None)

    while len(deq) != 1:
        head = deq.popleft()
        while head:
            head.next = deq[0]
            if head.left:
                deq.append(head.left)
            if head.right:
                deq.append(head.right)
            head = deq.popleft()
        deq.append(head)


# Validity of binary search tree
def is_bst(root: BinaryTreeNode) -> bool:

    def min_max_rec(this_node: BinaryTreeNode, min_val: Optional[int], max_val: Optional[int], level: bool):
        this_level = True
        if this_node is None:
            return None, None, True
        else:
            left_min_max = min_max_rec(this_node.left, min_val, max_val, level)
            right_min_max = min_max_rec(this_node.right, min_val, max_val, level)
            left_min = this_node.data if not left_min_max[0] else left_min_max[0]
            left_max = this_node.data if not left_min_max[1] else left_min_max[1]
            right_min = this_node.data if not right_min_max[0] else right_min_max[0]
            right_max = this_node.data if not right_min_max[1] else right_min_max[1]
            if left_max > this_node.data or right_min < this_node.data:
                this_level = False
            return left_min, right_max, all([left_min_max[2], right_min_max[2], this_level])

    return min_max_rec(root, None, None, True)[2]


# Convert Binary Tree to Doubly Linked List
# Recursive approach
def convert_to_linked_list(root: Optional[BinaryTreeNode]):

    def left_right(this_node) -> Tuple[BinaryTreeNode, BinaryTreeNode]:

        if this_node.left:
            pair_from_left = left_right(this_node.left)
            this_node.left = pair_from_left[0]
            pair_from_left[0].right = this_node
            most_right = pair_from_left[1]
        else:
            most_right = this_node

        if this_node.right:
            pair_from_right = left_right(this_node.right)
            this_node.right = pair_from_right[1]
            pair_from_right[1].left = this_node
            most_left = pair_from_right[0]
        else:
            most_left = this_node

        return most_left, most_right

    left_right(root)

    while root.left:
        root = root.left

    return root
