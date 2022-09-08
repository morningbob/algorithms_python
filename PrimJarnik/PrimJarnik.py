
import heapq

class Edge:
    def __init__(self, weight, start_vertex, end_vertex):
        self.weight = weight
        self.start_vertex = start_vertex
        self.end_vertex = end_vertex

    def __lt__(self, other):
        return self.weight < other.weight

class Node:
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.adj_list = []


class Prim_Jarnik:
    def __init__(self, vertex_list):
        self.vertex_list = vertex_list
        self.heap = []


    def find_minimum_spanning_tree(self, start_vertex):
        result_edges = []
        visited_nodes = 0
        total_cost = 0

        current_node = start_vertex
        current_node.visited = True
        visited_nodes += 1
        while visited_nodes < len(self.vertex_list):
            for edge in current_node.adj_list:
                if not edge.end_vertex.visited:
                    heapq.heappush(self.heap, edge)

            min_edge = heapq.heappop(self.heap)
            min_edge.end_vertex.visited = True
            total_cost += min_edge.weight
            visited_nodes += 1
            current_node = min_edge.end_vertex
            result_edges.append(min_edge)

        return result_edges, total_cost




