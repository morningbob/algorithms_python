
from Binary_Search_Tree import Binary_Search_Tree


if __name__ == '__main__':


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

    binary_search_tree.remove(25)

    binary_search_tree.traverse()




