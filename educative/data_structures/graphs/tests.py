from typing import Callable
import unittest

from solutions import *
from educative.data_structures.graphs.challenges.MinimumSpanningTree import *

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

    # Challenge 8: Find the Shortest Path Between Two Vertices
    def test_find_min(self):
        g = Graph(7)
        source_destination = [(0, 1), (0, 2), (0, 3), (2, 4), (3, 5), (5, 4)]
        for x in source_destination:
            g.add_edge(x[0], x[1])
        self.assertEqual(2, find_min(g, 0, 4))
        self.assertEqual(2, find_min(g, 3, 4))
        self.assertEqual(-1, find_min(g, 3, 6))

    def test_find_min_recursive(self):
        g = Graph(7)
        source_destination = [(0, 1), (0, 2), (0, 3), (2, 4), (3, 5), (5, 4)]
        for x in source_destination:
            g.add_edge(x[0], x[1])

        self.assertEqual(2, find_min_recursive(g, 0, 4))
        self.assertEqual(2, find_min_recursive(g, 3, 4))
        self.assertEqual(-1, find_min_recursive(g, 3, 6))

    # Clone a Directed Graph
    def test_clone(self):
        root = GraphNode(0)
        node_1 = GraphNode(1)
        node_2 = GraphNode(2)
        node_3 = GraphNode(3)
        node_4 = GraphNode(4)
        root.neighbors = [node_3, node_4]
        node_1.neighbors = [node_2]
        node_3.neighbors = [node_2]
        node_4.neighbors = [root, node_1, node_3]

        new_root = clone(root)
        self.assertEqual(0, new_root.data)
        self.assertEqual(3, new_root.neighbors[0].data)
        self.assertEqual(4, new_root.neighbors[1].data)

    # Tasks Scheduling
    def test_find_min_spanning_tree(self):
        vertices: List[Vertex] = [Vertex(x, False) for x in range(1, 6)]
        edges: List[Edge] = [
            Edge(1, False, vertices[0], vertices[1]),
            Edge(1, False, vertices[0], vertices[2]),
            Edge(2, False, vertices[1], vertices[2]),
            Edge(3, False, vertices[1], vertices[3]),
            Edge(3, False, vertices[2], vertices[4]),
            Edge(2, False, vertices[3], vertices[4]),
        ]
        g = TypedGraph(vertices, edges)

        self.assertEqual(7, g.find_min_spanning_tree())

    def test_is_scheduling_possible(self):
        def test(f: Callable):
            self.assertTrue(f(3, [[0, 1], [1, 2]]))
            self.assertFalse(f(3, [[0, 1], [1, 2], [2, 0]]))
            self.assertTrue(f(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]]))

        test(is_scheduling_possible_graph)
        test(is_scheduling_possible)

    def test_sorted_order(self):
        self.assertEqual(
            [0, 1, 2],
            find_order(3, [[0, 1], [1, 2]]))
        self.assertEqual(
            [],
            find_order(3, [[0, 1], [1, 2], [2, 0]]))
        self.assertEqual(
            [0, 1, 4, 3, 2, 5],
            find_order(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]]))

    def test_print_orders(self):
        example_1 = print_orders(3, [[0, 1], [1, 2]])
        self.assertTrue([0, 1, 2] in example_1)
        self.assertEqual(1, len(example_1))

        example_2 = print_orders(4, [[3, 2], [3, 0], [2, 0], [2, 1]])
        self.assertTrue([3, 2, 0, 1] in example_2)
        self.assertTrue([3, 2, 1, 0] in example_2)
        self.assertEqual(2, len(example_2))

        example_3 = print_orders(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])
        self.assertTrue([0, 1, 4, 3, 2, 5] in example_3)
        self.assertTrue([0, 1, 3, 4, 2, 5] in example_3)
        self.assertTrue([0, 1, 3, 2, 4, 5] in example_3)
        self.assertTrue([0, 1, 3, 2, 5, 4] in example_3)
        self.assertTrue([1, 0, 3, 4, 2, 5] in example_3)
        self.assertTrue([1, 0, 3, 2, 4, 5] in example_3)
        self.assertTrue([1, 0, 3, 2, 5, 4] in example_3)
        self.assertTrue([1, 0, 4, 3, 2, 5] in example_3)
        self.assertTrue([1, 3, 0, 2, 4, 5] in example_3)
        self.assertTrue([1, 3, 0, 2, 5, 4] in example_3)
        self.assertTrue([1, 3, 0, 4, 2, 5] in example_3)
        self.assertTrue([1, 3, 2, 0, 5, 4] in example_3)
        self.assertTrue([1, 3, 2, 0, 4, 5] in example_3)
        self.assertEqual(13, len(example_3))

    def test_alien_dictionary(self):
        input = ["ba", "bc", "ac", "cab"]
        self.assertEqual('bac', alien_dictionary(input))

        input = ["cab", "aaa", "aab"]
        self.assertEqual('cab', alien_dictionary(input))

        input = ["ywx", "wz", "xww", "xz", "zyy", "zwz"]
        self.assertEqual('ywxz', alien_dictionary(input))
