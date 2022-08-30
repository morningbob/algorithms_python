from Node import Node


class Binary_Search_Tree:

    def __init__(self):
        self.list = []
        self.parentNode = None

    # if the node exist, we first compare if the input node is greater than the
    # existing node, if it is smaller, we first check if there is a left child
    # if no, we add the left child
    def insert(self, data):
        if self.parentNode is None:
            newNode = Node(data)
            self.list.append(newNode)
            self.parentNode = newNode
        elif self.parentNode.data > data:
            # go to left child
            self.searchLeft(self.parentNode, data)
        elif self.parentNode.data < data:
            self.searchRight(self.parentNode, data)

    def searchLeft(self, node, data):
        if node.left_node is None:
            # add the child
            newNode = Node(data, node)
            self.list.append(newNode)
            # update the parent
            node.left_node = newNode
        elif node.left_node.data > data:
            self.searchLeft(node.left_node, data)

    def searchRight(self, node, data):
        if node.right_node is None:
            # add the child
            newNode = Node(data, node)
            self.list.append(newNode)
            # update the parent
            node.right_node = newNode
        elif node.right_node.data < data:
            self.searchRight(node.right_node, data)

    def inOrderTraversal(self):
        # we go to the left subtree, then, root, then right subtree
        if self.parentNode is not None:
            if self.parentNode.left_node is not None:
                # go to left node
                self.travseLeft(self.parentNode.left_node)
                print(" parent left node: ", self.parentNode.data)
            if self.parentNode.right_node is not None:
                # go to left node
                self.travseRight(self.parentNode.right_node)
                print(" parent right node: ", self.parentNode.data)

    def travseLeft(self, node):
        if node.left_node is not None:
            self.travserLeft(node.left_node)
        else:
            print("child node: ", node.data)

    def travseRight(self, node):
        if node.right_node is not None:
            self.travseRight(node.left_node)
        else:
            print("child node: ", node.data)

    def treeSize(self):
        print(len(self.list))

    def treeList(self):
        for i in self.list:
            print(i.data, " ")
            if i.left_node != None:
                print("left_node", i.left_node.data)
            if i.right_node != None:
                print("right_node", i.right_node.data)