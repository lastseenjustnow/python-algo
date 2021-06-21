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

    # Stack approach
    def test_dfs_traversal(self):
        graph = Graph(7)
        source_destination = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6)]
        for x in source_destination:
            graph.add_edge(x[0], x[1])
        expected_result = "1245360"
        function_output = dfs_traversal(graph, 1)
        self.assertEqual(expected_result, function_output)

    # Challenge 3: Detect Cycle in a Directed Graph
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

    # Challenge 4: "Mother Vertex" in a Directed Graph
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

    # Challenge 5: Count Number of Edges in an Undirected Graph
    def test_num_edges(self):
        g = UndirectedGraph(8)
        source_destination = [(0, 1), (0, 4), (1, 2), (1, 3), (2, 4), (2, 5), (3, 5), (4, 5), (5, 6), (5, 7), (6, 7)]
        for x in source_destination:
            g.add_edge(x[0], x[1])
        self.assertEqual(11, num_edges(g))

    # Challenge 6: Check if a Path Exists Between Two Vertices
    def test_check_path(self):
        g = Graph(8)
        source_destination = [(0, 1), (0, 4), (1, 2), (1, 3), (2, 5), (4, 2), (5, 3), (5, 6), (5, 7), (6, 7)]
        for x in source_destination:
            g.add_edge(x[0], x[1])
        self.assertTrue(check_path(g, 0, 6))
        self.assertTrue(check_path(g, 1, 7))
        self.assertFalse(check_path(g, 6, 3))

    # Challenge 7: Check if a Given Undirected Graph is Tree
    # Stack approach
    def test_is_tree(self):
        g = UndirectedGraph(5)
        source_destination = [(0, 1), (0, 2), (0, 3), (3, 4)]

        for x in source_destination:
            g.add_edge(x[0], x[1])
        self.assertTrue(is_tree(g))

        g.add_edge(4, 2)
        self.assertFalse(is_tree(g))

        g = UndirectedGraph(4)
        source_destination = [(0, 1), (0, 2), (0, 3), (3, 2)]
        for x in source_destination:
            g.add_edge(x[0], x[1])
        self.assertFalse(is_tree(g))

        g = UndirectedGraph(6)
        source_destination = [(0, 1), (0, 2), (0, 3), (3, 4)]

        for x in source_destination:
            g.add_edge(x[0], x[1])
        self.assertFalse(is_tree(g))

    def test_is_tree_recursive(self):
        g = UndirectedGraph(5)
        source_destination = [(0, 1), (0, 2), (0, 3), (3, 4)]

        for x in source_destination:
            g.add_edge(x[0], x[1])
        self.assertTrue(is_tree_recursive(g))

        g.add_edge(4, 2)
        self.assertFalse(is_tree_recursive(g))

        g = UndirectedGraph(4)
        source_destination = [(0, 1), (0, 2), (0, 3), (3, 2)]
        for x in source_destination:
            g.add_edge(x[0], x[1])
        self.assertFalse(is_tree_recursive(g))

        g = UndirectedGraph(6)
        source_destination = [(0, 1), (0, 2), (0, 3), (3, 4)]

        for x in source_destination:
            g.add_edge(x[0], x[1])
        self.assertFalse(is_tree_recursive(g))