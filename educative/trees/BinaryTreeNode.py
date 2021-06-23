from typing import List


class BinaryTreeNode:
    def __init__(self, data):
        self.left, self.right, self.next = None, None, None
        self.data = data


def create_BST(arr: List[int]):
    arr_len = len(arr)
    middle_point = int(arr_len/2)
    if arr_len == 0:
        return None
    else:
        btn = BinaryTreeNode(arr[middle_point])
        btn.left = create_BST(arr[:middle_point])
        btn.right = create_BST(arr[middle_point+1:])
        return btn

