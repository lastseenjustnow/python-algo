from typing import Optional, List, Tuple, Deque, Callable
from collections import deque
import sys
import pickle

from BinaryTreeNode import BinaryTreeNode
from NaryTreeNode import NaryTreeNode

# Check if Two Binary Trees are Identical
def are_identical(root1: BinaryTreeNode, root2: BinaryTreeNode) -> bool:
    if root1 is None and root2 is not None:
        return False
    if root1 is not None and root2 is None:
        return False
    if root1 is None and root2 is None:
        return True

    return are_identical(root1.left, root2.left) \
           and are_identical(root1.right, root2.right) \
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


# Print Tree Perimeter
def display_tree_perimeter(root: BinaryTreeNode) -> str:
    def empty_dec(dq: Deque[BinaryTreeNode], f1: Callable, f2: Callable, res: str):
        while dq:
            this_node = dq.popleft()
            while this_node:
                if f1(this_node):
                    dq.append(f1(this_node))
                if not (f2(this_node) or f1(this_node)):
                    res = ' '.join([res, str(this_node.data)])
                this_node = this_node.left
        return res

    result = str(root.data)
    deq: Deque[BinaryTreeNode] = deque()

    current_node = root.left if root.left else None
    while current_node:
        result = ' '.join([result, str(current_node.data)])
        if current_node.right:
            deq.append(current_node.right)
        current_node = current_node.left

    result = empty_dec(deq, lambda x: x.right, lambda x: x.left, result)

    current_node = root.right if root.right else None
    to_append = ''
    while current_node.right:
        to_append = ' '.join([str(current_node.data), to_append])
        if current_node.right:
            deq.append(current_node.right)
        current_node = current_node.right

    result = ' '.join([empty_dec(deq, lambda x: x.left, lambda x: x.right, result), to_append])

    return result


# Connect All Siblings of a Binary Tree
def populate_sibling_pointers(root: BinaryTreeNode):
    deq = deque()
    previous = None
    deq.append(root)

    while deq:
        current = deq.popleft()
        if previous:
            previous.right = current
        if current.left:
            deq.append(current.left)
        if current.right:
            deq.append(current.right)
        previous = current

    return root


# Serialize/Deserialize Binary Tree
def serialize(node, stream):
    MARKER = sys.maxsize
    if node == None:
        stream.dump(MARKER)
        return
    stream.dump(node.data)
    serialize(node.left, stream)
    serialize(node.right, stream)


def deserialize(stream):
    MARKER = sys.maxsize
    try:
        data = pickle.load(stream)
        if data == MARKER:
            return None

        node = BinaryTreeNode(data)
        node.left = deserialize(stream)
        node.right = deserialize(stream)
        return node
    except pickle.UnpicklingError:
        return None


# Nth Highest Number in Binary Search Tree
def find_nth_highest_in_bst(node: BinaryTreeNode, n) -> Optional[BinaryTreeNode]:
    deq: Deque[BinaryTreeNode] = deque()

    while node:
        deq.append(node)
        node = node.right

    count = 0
    current_node = None
    while count != n:
        if len(deq) == 0:
            return None
        current_node = deq.pop()
        if current_node.left:
            left_subtree = current_node.left
            deq.append(left_subtree)
            while left_subtree.right:
                deq.append(left_subtree.right)
                left_subtree = left_subtree.right
        count += 1

    return current_node


# Mirror Binary Tree Nodes
# Stack approach
def mirror_tree(root):

    deq = deque()
    deq.append(root)

    while deq:
        current_node = deq.pop()
        if current_node.left:
            deq.append(current_node.left)
        if current_node.right:
            deq.append(current_node.right)
        current_left_subtree = current_node.left if current_node.left else None
        current_right_subtree = current_node.right if current_node.right else None
        current_node.left, current_node.right = current_right_subtree, current_left_subtree

    return root


# Recursive approach
def mirror_tree_rec(root: BinaryTreeNode):

    if not root:
        return None
    else:
        current_left_subtree = mirror_tree_rec(root.left) if root.left else None
        current_right_subtree = mirror_tree_rec(root.right) if root.right else None
        root.left, root.right = current_right_subtree, current_left_subtree
        return root


# Delete Zero Sum Sub-Trees
def delete_zero_sum_subtree(root):

    def go(root: BinaryTreeNode) -> int:
        if root is None:
            return 0
        else:
            left_subsum = go(root.left)
            right_subsum = go(root.right)
            if left_subsum == 0:
                root.left = None
            if right_subsum == 0:
                root.right = None
            return left_subsum + right_subsum + root.data

    go(root)
    return root


# Convert N-ary Tree to Binary Tree
def convert_n_ary_to_binary(node: NaryTreeNode) -> BinaryTreeNode:

    def convert_rec(this_node: BinaryTreeNode, children: List[NaryTreeNode], flag_value: int):
        current_node = this_node
        for child in children:
            if flag_value == 0:
                current_node.left = BinaryTreeNode(child.data)
                current_node = current_node.left
                convert_rec(current_node, child.children, 1 - flag_value)
            else:
                current_node.right = BinaryTreeNode(child.data)
                current_node = current_node.right
                convert_rec(current_node, child.children, 1 - flag_value)

    binary_node = BinaryTreeNode(node.data)
    convert_rec(binary_node, node.children, 0)

    return binary_node


# Minimum Depth of a Binary Tree (easy)
# Recursive approach
def find_minimum_depth(root: BinaryTreeNode):
    def rec(r: BinaryTreeNode, current_depth: int):
        if not (r.left or r.right):
            return current_depth + 1
        elif r.left and r.right:
            return min(rec(r.left, current_depth + 1), rec(r.right, current_depth + 1))
        elif r.left:
            return rec(r.left, current_depth + 1)
        else:
            return rec(r.right, current_depth + 1)

    return rec(root, 0)


# All Paths for a Sum
def find_paths(root: BinaryTreeNode, summ: int):
    allPaths = []

    def rec(root: BinaryTreeNode, current_path: List[int]):
        s = sum(current_path)
        if not root or s + root.data > summ:
            return
        elif s + root.data == summ:
            allPaths.append([*current_path, root.data])
            return
        else:
            new_path = [*current_path, root.data]
            rec(root.left, new_path)
            rec(root.right, new_path)

    rec(root, [])

    return allPaths
