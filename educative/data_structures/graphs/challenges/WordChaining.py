import unittest

class vertex:
    def __init__(self, value, visited):
        self.value = value
        self.visited = visited
        self.adj_vertices = []
        self.in_vertices = []


class graph:
    g = []

    def __init__(self, g):
        self.g = g

    # This method creates a graph from a list of words. A node of
    # the graph contains a character representing the start or end
    # character of a word.
    def create_graph(self, words_list):
        for i in range(len(words_list)):
            word = words_list[i]
            start_char = word[0]
            end_char = word[len(word) - 1]

            start = self.vertex_exists(start_char)

            if start is None:
                start = vertex(start_char, False)
                self.g.append(start)

            end = self.vertex_exists(end_char)
            if end is None:
                end = vertex(end_char, False)
                self.g.append(end)

            # Add an edge from start vertex to end vertex
            self.add_edge(start, end)

    # This method returns the vertex with a given value if it
    # already exists in the graph, returns NULL otherwise
    def vertex_exists(self, value):
        for i in range(len(self.g)):
            if self.g[i].value == value:
                return self.g[i]
        return None

    # This method returns TRUE if all nodes of the graph have
    # been visited
    def all_visited(self):
        for i in range(len(self.g)):
            if not self.g[i].visited:
                return False
        return True

    # This method adds an edge from start vertex to end vertex by
    # adding the end vertex in the adjacency list of start vertex
    # It also adds the start vertex to the in_vertices of end vertex
    def add_edge(self, start, end):
        start.adj_vertices.append(end)
        end.in_vertices.append(start)

    # This method returns TRUE if out degree of each vertex is equal
    # to its in degree, returns FALSE otherwise
    def out_equals_in(self):
        for i in range(len(self.g)):
            out = len(self.g[i].adj_vertices)
            inn = len(self.g[i].in_vertices)
            if out != inn:
                return False
        return True

    # This method returns TRUE if the graph has a cycle containing
    # all the nodes, returns FALSE otherwise
    def can_chain_words_rec(self, node, starting_node):
        node.visited = True

        # Base case
        # return TRUE if all nodes have been visited and there
        # exists an edge from the last node being visited to
        # the starting node
        adj = node.adj_vertices
        if self.all_visited():
            for i in range(len(adj)):
                if adj[i] == starting_node:
                    return True

        # Recursive case
        for i in range(len(adj)):
            if not adj[i].visited:
                node = adj[i]
                if self.can_chain_words_rec(node, starting_node):
                    return True
        return False

    def can_chain_words(self, list_size):
        # Empty list and single word cannot form a chain
        if list_size <= 1:
            return False

        return self.can_chain_words_rec(self.g[0], self.g[0])

    def print_graph(self):
        for i in range(len(self.g)):
            print(self.g[i].value + " " + str(self.g[i].visited) + "\n")
            adj = self.g[i].adj_vertices
            for j in range(len(adj)):
                print(adj[j].value + " ")
            print("\n")


class TestWordChaining(unittest.TestCase):
    def test_can_chain_words(self):
        g = graph([])
        g.create_graph(['eve', 'eat', 'ripe', 'tear'])
        print(g.can_chain_words(4))
