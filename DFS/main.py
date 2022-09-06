# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from DFS import DFS, Node

if __name__ == '__main__':

    dfs = DFS()

    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")

    # handle and set the neighbors accordingly
    node1.adj_list.append(node2)
    node1.adj_list.append(node3)
    node2.adj_list.append(node4)
    node4.adj_list.append(node5)



    dfs.print_nodes(dfs.DFS(node1))



