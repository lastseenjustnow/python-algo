from typing import List


class GraphNode:
    def __init__(self, d: int):
        self.data: int = d
        self.neighbors: List[GraphNode] = []
