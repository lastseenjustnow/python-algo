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

    def test_detect_cycle_recursive(self):
        graph = Graph(7)
        source_destination = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6)]
        for x in source_destination:
            graph.add_edge(x[0], x[1])
        self.assertFalse(detect_cycle(graph))

        graph.add_edge(6, 1)
        self.assertTrue(detect_cycle(graph))

        graph = Graph(3)
        source_destination = [(0, 1), (1, 2)]
        for x in source_destination:
            graph.add_edge(x[0], x[1])
        self.assertFalse(detect_cycle(graph))

        graph.add_edge(2, 0)
        self.assertTrue(detect_cycle(graph))

    def test_find_mother_vertex(self):
        g = Graph(3)
        source_destination = [(0, 1), (1, 2), (2, 0)]
        for x in source_destination:
            g.add_edge(x[0], x[1])

        g = Graph(4)
        source_destination = [(3, 0), (3, 1), (1, 1)]
        for x in source_destination:
            g.add_edge(x[0], x[1])
        self.assertEqual(3, find_mother_vertex(g))

        graph = Graph(7)
        source_destination = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6)]
        for x in source_destination:
            graph.add_edge(x[0], x[1])
        self.assertEqual(-1, find_mother_vertex(graph))