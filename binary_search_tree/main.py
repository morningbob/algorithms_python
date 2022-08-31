# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from Binary_Search_Tree import Binary_Search_Tree
from Node import Node

if __name__ == '__main__':

    #node = Node()

    binary_search_tree = Binary_Search_Tree()

    binary_search_tree.insert(10)
    binary_search_tree.insert(2)
    binary_search_tree.insert(5)
    binary_search_tree.insert(9)
    binary_search_tree.insert(25)
    binary_search_tree.insert(3)
    binary_search_tree.insert(20)
    binary_search_tree.insert(4)

    binary_search_tree.traverse()

    print("Max Node: ", binary_search_tree.getMaxNode())
    print("Min Node: ", binary_search_tree.getMinNode())

    binary_search_tree.printNode(binary_search_tree.root)

    binary_search_tree.printNode(binary_search_tree.root.left_node)



