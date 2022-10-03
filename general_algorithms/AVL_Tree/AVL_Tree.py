from Node import Node


class AVL_Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            newNode = Node(data)
            self.root = newNode
        else:
            self.insertNewNode(self.root, data)

    # we calculate the height of the node when we insert to the node a child
    def insertNewNode(self, node, data):
        if node.data > data:
            if node.left_node is None:
                newNode = Node(data, node)
                node.left_node = newNode
                node.height = max(self.getHeight(node.left_node), self.getHeight(node.right_node)) + 1
            else:
                self.insertNewNode(node.left_node, data)
        elif node.data < data:
            if node.right_node is None:
                newNode = Node(data, node)
                node.right_node = newNode
                node.height = max(self.getHeight(node.left_node), self.getHeight(node.right_node)) + 1
            else:
                self.insertNewNode(node.right_node, data)

        self.check_properties(node)
        #print("checked properites", self.check_properties(node))

    def remove(self, data):
        if self.root:
            print("remove", "root is not null")
            self.removeNode(data, self.root)

    def removeNode(self, data, node):
        # search for the data first
        # case 1, leaf node, just remove it
        # case 2, node with 1 child, update the left_node and right node
        # case 3, node with 2 children,

        # we get the parent of the node to be removed, to check if the
        # tree is still balanced

        parent = node.parent

        if node.data > data:
            print("node ", node.data, "is greater than the data", data)
            self.removeNode(data, node.left_node)
        elif node.data < data:
            print("node ", node.data, "is smaller than the data", data)
            self.removeNode(data, node.right_node)
        elif node.data == data:
            print("the node ", node.data, " == ", "data", data)
            # case that the node is a leaf node with no child
            if node.left_node is None and node.right_node is None:
                print("felt into leaf node case")
                if node.parent and node.parent.right_node == node:
                    node.parent.right_node = None
                elif node.parent and node.parent.left_node == node:
                    node.parent.left_node = None
                elif node.parent is None:
                    self.root = None

                del node
            # case that the node to be removed has only 1 left child
            elif node.left_node is not None and node.right_node is None:
                print("node ", node.data, "left node is not null")
                # update the parent node's left node to the child
                if node.parent.left_node == node:
                    node.parent.left_node = node.left_node
                if node.parent.right_node == node:
                    node.parent.right_node = node.left_node
                # update the child's parent node to the parent
                node.left_node.parent = node.parent
                del node
            # case that the node to be removed has only 1 right child
            elif node.right_node is not None and node.left_node is None:
                print("node ", node.data, "right node is not null")
                # update the parent node's right node to the child
                if node.parent and node.parent.left_node == node:
                    node.parent.left_node = node.right_node
                if node.parent and node.parent.right_node == node:
                    node.parent.right_node = node.right_node
                # update the child's parent node to the parent
                node.right_node.parent = node.parent
                del node
            elif node.left_node is not None and node.right_node is not None:
                print("node ", node.data, "both nodes are not null")
                # get predecessor - get the largest node in the left subtree
                predecessorNode = self.getPredecessor(node.left_node)
                print("predecessor node ", predecessorNode.data)
                # switch the node to be removed with the predecessorNode
                # we can just switch the content of the nodes
                # in this case, is the data

                tempNodeData = node.data
                node.data = predecessorNode.data
                predecessorNode.data = tempNodeData

                self.removeNode(data, predecessorNode)

        self.check_properties(parent)
        #print("checked properites", self.checkProperties(node))

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
        print("Node: ", node.data, "height: ", node.height)

        if node.right_node is not None:
            self.inOrderTraversal(node.right_node)

    def getMaxNode(self):
        if self.root:
            return self.getMax(self.root)

    def getMax(self, node):
        if node.right_node:
            print("traversed ", node.data, "right node exist: ", node.right_node.data)
            return self.getMax(node.right_node)

        return node.data

    def getMinNode(self):
        if self.root:
            return self.getMin(self.root)

    def getMin(self, node):
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
    # the predecessor is the largest node of the left subtree
    def getPredecessor(self, node):
        if node.right_node is not None:
            return self.getPredecessor(node.right_node)

        return node

    def getHeight(self, node):
        if node is None:
            return -1

        return node.height

    def getBalanceFactor(self, node):
        # we can't just access the height field
        # we access the dynamic height
        result = self.getHeight(node.left_node) - self.getHeight(node.right_node)
        print("node ", node.data, " balance factor ", result)
        return result

    def check_properties(self, node):
        while node is not None:
            node.height = max(self.getHeight(node.left_node), self.getHeight(node.right_node)) + 1
            self.checkBalanceFactor(node)
            node = node.parent

    # this method checks if the AVL tree is balanced, by calculating the balance factor
    # it checks the nodes recursively until it reaches the root node
    def checkBalanceFactor(self, node):
        print("checking properties")
        if node is None:
            print("reached root node")
            return

        balFactor = self.getBalanceFactor(node)

        # balance factor greater than 1 means the node's tree is left heavy
        if balFactor > 1:
            # here we need to check if the left child of the node is balanced
            # we can rotate it here first if it is right heavy
            # we compare to 0 because the node is one level up than the child
            if self.getBalanceFactor(node.left_node) < 0:
                # it is right heavy in the left child tree
                # rotate left child tree to the left first
                self.rotate_left(node.left_node)

            # if the child is right heavy in the left child, the above if clause
            # is executed, then, we rotate the node's tree itself to the right.
            # if the child is not right heavy, the above clause will be skipped
            self.rotate_right(node)

        # balance factor is smaller than -1 mean the node's tree is right heavy
        if balFactor < -1:
            # here we check if the right child is left heavy
            if self.getBalanceFactor(node.right_node) > 0:
                # if is left heavy in the right child tree
                # rotate right child tree to the right first
                self.rotate_right(node.right_node)

            # the above rotation will be skipped if the child is not left heavy
            self.rotate_left(node)


    def rotate_right(self, node):
        print("rotating right for node", node.data)
        # update the ref of the nodes
        future_parent_node = node.left_node
        grand_parent_node = node.parent
        future_parent_right_child = future_parent_node.right_node
        # update current parent
        node.left_node = future_parent_right_child
        node.parent = future_parent_node
        node.height = max(self.getHeight(node.left_node), self.getHeight(node.right_node)) + 1
        # update current parent's left child
        future_parent_node.parent = grand_parent_node
        future_parent_node.right_node = node
        future_parent_node.height = max(self.getHeight(future_parent_node.left_node),
                                        self.getHeight(future_parent_node.right_node)) + 1
        # update the ref of a child node
        if future_parent_right_child is not None:
            future_parent_right_child.parent = node
        # update grand parent
        if grand_parent_node is not None and grand_parent_node.left_node == node:
            grand_parent_node.left_node = future_parent_node
        if grand_parent_node is not None and grand_parent_node.right_node == node:
            grand_parent_node.right_node = future_parent_node
        # that we need to consider the case where the node to rotate is already root node
        if node == self.root:
            self.root = future_parent_node


    def rotate_left(self, node):
        print("rotating left for node", node.data)
        future_parent_node = node.right_node
        grand_parent_node = node.parent
        future_parent_left_node = future_parent_node.left_node
        # update current parent
        node.right_node = future_parent_left_node
        node.parent = future_parent_node
        node.height = max(self.getHeight(node.left_node), self.getHeight(node.right_node)) + 1
        # update current parent's left child
        future_parent_node.parent = grand_parent_node
        future_parent_node.left_node = node
        future_parent_node.height = max(self.getHeight(future_parent_node.left_node),
                                        self.getHeight(future_parent_node.right_node)) + 1
        # update the ref of a child node
        if future_parent_left_node is not None:
            future_parent_left_node.parent = node
        # update grand parent
        if grand_parent_node is not None and grand_parent_node.left_node == node:
            grand_parent_node.left_node = future_parent_node
        if grand_parent_node is not None and grand_parent_node.right_node == node:
            grand_parent_node.right_node = future_parent_node
        # that we need to consider the case where the node to rotate is already root node
        if node == self.root:
            self.root = future_parent_node

    # current parent will be the right child of it's left child
    # left child became the parent
    #def rotateRight(self, node):
        # update current parent
        #node.left_node = None
        # update current parent's left child
        #node.left_node.parent = None
        

    # current parent will be the left child of it's right child
    # right child became the parent
    #def rotateLeft(self):




    # if the balance factor is positive and more than 1
    # need to rotate to the right

    # rotate right
    # case 1: left heavy only, or right heavy only
    # case 2: left right heavy, or right left heavy, 2 rotation

    #def rotateRight(self):
        # shift the node to the right, the node became the parent node
        # it's right most node in the left subtree became the child of the
            # parent of the right subtree





