import unittest

from solutions import *


class TestGraphSolution(unittest.TestCase):
    # Challenge 1: Implement Breadth First Search
    def test_bfs_traversal(self):
        graph = Graph(5)
        source_destination = [(0, 1), (0, 2), (1, 3), (1, 4)]
        for x in source_destination:
            graph.add_edge(x[0], x[1])
        expected_result = "02143"
        function_output = bfs_traversal(graph, 0)
        self.assertEqual(expected_result, function_output)

    # Challenge 2: Depth First Search
    def test_dfs_traversal_recursive(self):
        graph = Graph(7)
        source_destination = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6)]
        for x in source_destination:
            graph.add_edge(x[0], x[1])
        expected_result = "1362540"
        function_output = dfs_traversal_recursive(graph, 1)
        self.assertEqual(expected_result, function_output)

    def test_dfs_traversal(self):
        graph = Graph(7)
        source_destination = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6)]
        for x in source_destination:
            graph.add_edge(x[0], x[1])
        expected_result = "1245360"
        function_output = dfs_traversal(graph, 1)
        self.assertEqual(expected_result, function_output)
