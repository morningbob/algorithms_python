
class Node:

    def __init__(self, name):
        self.name = name
        self.adj_list = []
        self.visited = False


class DFS:

    def __init__(self):
        self.list = []

    def DFS(self, node):
        # list can be used as a stack,
        # with append to add and pop to get last item
        stack = [node]
        visit_route = []

        while len(stack) != 0:
            current_node = stack.pop()
            if current_node.visited:
                continue
            visit_route.append(current_node)
            for item in current_node.adj_list:
                if not item.visited:
                    stack.append(item)

        return visit_route

    def print_nodes(self, route):
        for item in route:
            print(item.name, " ", end="")
