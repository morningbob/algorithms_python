# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from Binary_Search_Tree import Binary_Search_Tree
from Node import Node

if __name__ == '__main__':

    #node = Node()

    binary_search_tree = Binary_Search_Tree()

    binary_search_tree.insert(1)
    binary_search_tree.insert(2)
    binary_search_tree.insert(3)


    binary_search_tree.treeSize()

    binary_search_tree.treeList()

    binary_search_tree.inOrderTraversal()

