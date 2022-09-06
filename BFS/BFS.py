from queue import Queue


class Node:

    def __init__(self, name):
        self.name = name
        self.adj_list = []
        self.visited = False


class BFS:

    def __init__(self):
        self.node_list = []

    def insert_node(self, node):
        self.node_list.append(node)
        print("added node", node.name)

    def BFS(self, node):

        queue = Queue()
        queue.put(node)

        visited_route = []

        while not queue.empty():
            current_node = queue.get()
            if current_node.visited:
                print("node visited", current_node.name)
                continue
            current_node.visited = True
            visited_route.append(current_node)
            # add node's neighbors to the queue
            for item in current_node.adj_list:
                if not item.visited:
                    queue.put(item)
                    print("node added to queue", item.name)

        return visited_route

    def print_nodes(self, node_list):
        for item in node_list:
            print(item.name, " ", end="")



