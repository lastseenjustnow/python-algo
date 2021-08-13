import unittest

from solutions import *

g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)


class TestGraphAlgorithmsSolution(unittest.TestCase):
    def test_number_of_nodes(self):
        self.assertEqual(1, number_of_nodes(g, 1))
        self.assertEqual(2, number_of_nodes(g, 2))
        self.assertEqual(2, number_of_nodes(g, 3))

    def test_transpose(self):
        new_g = transpose(g)
        self.assertIsNone(new_g.graph[0])
        self.assertEqual(0, new_g.graph[1].vertex)
        self.assertEqual(0, new_g.graph[2].vertex)
        self.assertEqual(1, new_g.graph[3].vertex)
        self.assertEqual(1, new_g.graph[4].vertex)

    def test_find_all_paths(self):
        g = Graph(5)
        edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [3, 5], [4, 5]]
        g.create_graph(edges)
        expected_result = [[0, 2, 5], [0, 1, 4, 5], [0, 1, 3, 5]]
        self.assertEqual(expected_result, find_all_paths(g, 0, 5))
