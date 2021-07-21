from typing import List


class NaryTreeNode:
    def __init__(self, data):
        self.children: List[NaryTreeNode] = []
        self.data = data