from typing import List

from educative.data_structures.linked_lists.LinkedList import LinkedList


class Graph:
    def __init__(self, vertices):
        # Total number of vertices
        self.vertices = vertices
        # defining a list which can hold multiple LinkedLists
        # equal to the number of vertices in the graph
        self.array: List[LinkedList] = []
        # Creating a new Linked List for each vertex/index of the list
        for i in range(vertices):
            self.array.append(LinkedList())

    # Function to add an edge from source to destination
    def add_edge(self, source, destination):
        if source < self.vertices and destination < self.vertices:
            # As we are implementing a directed graph, (1,0) is not equal to (0,1)
            self.array[source].insert_at_head(destination)

    def print_graph(self):
        print(">>Adjacency List of Directed Graph<<")
        for i in range(self.vertices):
            print("|", i, end=" | => ")
            temp = self.array[i].get_head()
            while temp is not None:
                print("[", temp.data, end=" ] -> ")
                temp = temp.next_element
            print("None")


class UndirectedGraph(Graph):
    def add_edge(self, source, destination):
        if source < self.vertices and destination < self.vertices:
            self.array[source].insert_at_head(destination)
            self.array[destination].insert_at_head(source)
