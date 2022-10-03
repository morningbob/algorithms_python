
class Node:
    def __init__(self, data, parent = None):
        self.parent = parent
        self.data = data
        self.left_node = None
        self.right_node = None
        self.height = 0

