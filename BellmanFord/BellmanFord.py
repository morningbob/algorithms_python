from queue import Queue


class Edge:
    def __init__(self, weight, start_vertex, end_vertex):
        self.weight = weight
        self.start_vertex = start_vertex
        self.end_vertex = end_vertex


class Node:
    def __init__(self, name):
        self.name = name
        self.adj_list = []
        self.min_distance = float('inf')
        self.visited = False
        self.predecessor = None


class Bellman_Ford:
    def __init__(self, vertice, edges, start_vertex):
        self.vertice = vertice
        self.edges = edges
        self.start_vertex = start_vertex
        self.has_cycle = False

    def Bellman_Ford(self):
        # we iterate through every edge
        # try to update the min_distance
        # the min_distance will be updated starting from the start node to the other nodes
        # outer loop is the number of times we go through every edge
        for i in range(len(self.vertice) - 1):
            self.start_vertex.min_distance = 0
            for edge in self.edges:
                u = edge.start_vertex
                v = edge.end_vertex

                new_distance = u.min_distance + edge.weight
                if new_distance < v.min_distance:
                    # update distance
                    v.min_distance = new_distance
                    v.predecessor = u

        for edge in self.edges:
            cycle = self.detect_cycle(edge)
            if cycle:
                print("negative cycle detected")
                return



    def get_shortest_path(self, end_node):
        if not self.has_cycle:
            node = end_node
            print("the total min distance is: ", node.min_distance)
            while node is not None:
                print("node", node.name)
                node = node.predecessor
        else:
            print("the graph has negative cycle")



    def detect_cycle(self, edge):
       if (edge.start_vertex.min_distance + edge.weight) < edge.end_vertex.min_distance:
           self.has_cycle = True
           return True
       else:
           return False







