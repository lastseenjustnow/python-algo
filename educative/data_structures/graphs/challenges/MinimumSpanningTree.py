from typing import List, Optional


class Vertex:
    def __init__(self, id, visited):
        self.id = id
        self.visited = visited


class Edge:
    def __init__(self, weight, visited, src: Vertex, dest: Vertex):
        self.weight = weight
        self.visited = visited
        self.src = src
        self.dest = dest


class TypedGraph:
    g: List[Vertex] = []  # vertices
    e: List[Edge] = []  # edges

    def __init__(self, g, e):
        self.g = g
        self.e = e

    def add_vertex(self, this: Vertex):
        self.g.append(this)

    def add_edge(self, this: Edge):
        self.e.append(this)
        src_vertex: Vertex = self.vertex_exists(this.src.id)
        dest_vertex: Vertex = self.vertex_exists(this.dest.id)
        for vertex in [src_vertex, dest_vertex]:
            if vertex.min_weight_edge is None or vertex.min_weight_edge.weight > this.weight:
                vertex.min_weight_edge = this

    # This method returns the vertex with a given id if it
    # already exists in the graph, returns NULL otherwise
    def vertex_exists(self, id):
        for i in range(len(self.g)):
            if self.g[i].id == id:
                return self.g[i]
        return None

    # This method generates the graph with v vertices
    # and e edges
    def generate_graph(self, vertices, edges):
        # create vertices
        for i in range(vertices):
            v = Vertex(i + 1, False)
            self.g.append(v)

        # create edges
        for i in range(len(edges)):
            src = self.vertex_exists(edges[i][1])
            dest = self.vertex_exists(edges[i][2])
            e = Edge(edges[i][0], False, src, dest)
            self.e.append(e)

    def find_min_spanning_tree(self):
        # Dijkstra-Jarník-Prim algorithm
        # Improve algorithm with heaps for minimum values!

        weight = 0
        initial_vertex: Vertex = self.g[0]
        initial_vertex.visited = True

        for _ in range(len(self.g)-1):
            min_weight_edge: Optional[Edge] = None
            for edge in self.e:
                if not edge.visited and ((edge.src.visited and not edge.dest.visited) or (not edge.src.visited and edge.dest.visited)) and (min_weight_edge is None or min_weight_edge.weight > edge.weight):
                    min_weight_edge = edge
            weight += min_weight_edge.weight
            min_weight_edge.visited = True
            for vertex in [min_weight_edge.src, min_weight_edge.dest]:
                vertex.visited = True

        return weight

    def print_graph(self):
        for i in range(len(self.g)):
            print(str(self.g[i].id) + " " + str(self.g[i].visited) + "\n")

        for i in range(len(self.e)):
            print(str(self.e[i].src.id) + "->" + str(self.e[i].dest.id) + "[" + str(self.e[i].weight) + ", " + str(
                self.e[i].visited) + "]  ")

        print("\n")

    def get_graph(self):
        res = ""
        for i in range(len(self.e)):
            if (i == len(self.e) - 1):
                res += "[" + str(self.e[i].src.id) + "->" + str(self.e[i].dest.id) + "]"
            else:
                res += "[" + str(self.e[i].src.id) + "->" + str(self.e[i].dest.id) + "],"
        return res

    def print_mst(self, w):
        print("MST")
        for i in range(len(self.e)):
            if self.e[i].visited:
                print(str(self.e[i].src.id) + "->"
                      + str(self.e[i].dest.id))

        print("weight: " + str(w))
        print("\n")
