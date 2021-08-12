import unittest

from solutions import *


class TestGraphAlgorithmsSolution(unittest.TestCase):
    def test_number_of_nodes(self):
        g = Graph(5)
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(1, 3)
        g.add_edge(1, 4)
        self.assertEqual(1, number_of_nodes(g, 1))
        self.assertEqual(2, number_of_nodes(g, 2))
        self.assertEqual(2, number_of_nodes(g, 3))
