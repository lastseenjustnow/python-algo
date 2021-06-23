from typing import Optional, List, Deque
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