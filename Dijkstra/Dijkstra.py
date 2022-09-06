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
        self.visited = False
        self.predecessor = None
        self.min_distance = float('inf')

    def __lt__(self, other):
        return self.min_distance < other.min_distance


class Dijkstra:
    def __init__(self):
        self.list = []

    # we need to update the min distance from the starting point to the node
    # we need to set the node visited
    # we need to update the predecessor of the node

    def dijkstra(self, node):

        queue = Queue()
        queue.put(node)
        node.min_distance = 0

        while not queue.empty():
            current_node = queue.get()
            if current_node.visited:
                continue
            for edge in current_node.adj_list:
                if not edge.end_vertex.visited:
                    current_distance = current_node.min_distance + edge.weight
                    # update min distance
                    if current_distance < edge.end_vertex.min_distance:
                        edge.end_vertex.min_distance = current_distance
                        # update predecessor
                        edge.end_vertex.predecessor = current_node
                    # we set the end vertex to be explored
                    queue.put(edge.end_vertex)

            current_node.visited = True


    def get_shortest_path(self, end_node):
        route = []
        node = end_node
        while node is not None:

            route.append(node)
            print("added node", node.name)
            node = node.predecessor

        for node in route:
            print("node ", node.name, "distance", node.min_distance)





