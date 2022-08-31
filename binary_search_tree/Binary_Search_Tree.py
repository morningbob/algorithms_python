from Node import Node


class Binary_Search_Tree:

    def __init__(self):
        self.root = None

    # if the node exist, we first compare if the input node is greater than the
    # existing node, if it is smaller, we first check if there is a left child
    # if no, we add the left child
    def insert(self, data):
        if self.root is None:
            newNode = Node(data)
            self.root = newNode
        else:
            self.insertNewNode(self.root, data)


    def insertNewNode(self, node, data):
        if node.data > data:
            if node.left_node is None:
                newNode = Node(data, node)
                node.left_node = newNode
            else:
                self.insertNewNode(node.left_node, data)
        elif node.data < data:
            if node.right_node is None:
                newNode = Node(data, node)
                node.right_node = newNode
            else:
                self.insertNewNode(node.right_node, data)

    def remove(self, data):
        if self.root:
            self.removeNode(data, self.root)

    def removeNode(self, data, node):
        # search for the data first
        # case 1, leaf node, just remove it
        # case 2, node with 1 child, update the left_node and right node
        # case 3, node with 2 children,
            # get predecessor
            # switch nodes
            # update left_node right_node
        if node.data > data:
            self.removeNode(data, node.left_node)
        elif node.data < data:
            self.removeNode(data, node.right_node)
        elif node.data == data:
            # case that the node is a leaf node with no child
            if node.left_node is None and node.right_node is None:
                if node.parent.right_node == node:
                    node.parent.right_node = None
                elif node.parent.left_node == node:
                    node.parent.left_node = None
            # case that the node to be removed has only 1 left child
            elif node.left_node is not None and node.right_node is None:
                # update the parent node's left node to the child
                node.parent = node.left_node
                # update the child's parent node to the parent
                node.left_node.parent = node.parent
            # case that the node to be removed has only 1 right child
            elif node.right_node is not None and node.left_node is None:
                # update the parent node's right node to the child
                node.parent = node.right_node
                # update the child's parent node to the parent
                node.right_node.parent = node.parent
            elif node.left_node is not None and node.right_node is not None:
                # get predecessor - get the largest node in the left subtree
                predecessorNode = self.getPredecessor(node)
                # switch the node to be removed with the predecessorNode
                # update the left_node and right_node and parent of the nodes
                # around the nodes
                # update the node's parent node left or right_node
                rootNodeToSwitch = self.root
                if node.parent.left_node == node:
                    node.parent.left_node = rootNodeToSwitch
                elif node.parent.right_node == node:
                    node.parent.right_node = rootNodeToSwitch
                # update the node's child node's parent field
                node.left_node.parent = rootNodeToSwitch
                node.right_node.parent = rootNodeToSwitch

                # update the child of root node







    def traverse(self):
        if self.root is None:
            print("tree is empty")
        else:
            self.inOrderTraversal(self.root)

    def inOrderTraversal(self, node):
        if node.left_node is not None:
            self.inOrderTraversal(node.left_node)

        # when the program reach a case when node.left_node is none,
        # it will execute this print
        print("Node: ", node.data)

        if node.right_node is not None:
            self.inOrderTraversal(node.right_node)

    def getMaxNode(self):
        if self.root:
            return self.getMax(self.root)

    def getMax(self, node):
        #print("getMax ran")
        #print("getMax, node ", node.data)
        if node.right_node:
            print("traversed ", node.data, "right node exist: ", node.right_node.data)
            return self.getMax(node.right_node)

        return node.data

    def getMinNode(self):
        if self.root:
            return self.getMin(self.root)

    def getMin(self, node):
        #print("getMin ran")
        #print("getMin, node ", node.data)
        if node.left_node:
            print("traversed ", node.data, "left node exits: ", node.left_node.data)
            return self.getMin(node.left_node)

        return node.data

    def printNode(self, node):
        if node.left_node is not None:
            print("Node ", node.data, " - left node", node.left_node.data)
        if node.right_node is not None:
            print("Node ", node.data, " - right node", node.right_node.data)

    # we need to get predecessor to switch the node to be removed with root node
    def getPredecessor(self, node):
        return False

