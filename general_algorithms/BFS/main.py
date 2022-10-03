# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from BFS import Node, BFS

if __name__ == '__main__':

    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")

    # we have to handle the neighbors
    node1.adj_list.append(node2)
    node1.adj_list.append(node3)
    node2.adj_list.append(node4)
    node4.adj_list.append(node5)

    bfs = BFS()
    bfs.print_nodes(bfs.BFS(node1))

    node5 = Node("A")
    node6 = Node("B")
    node7 = Node("C")
    node8 = Node("D")
    node9 = Node("E")
    node10 = Node("F")
    node11 = Node("G")
    node12 = Node("H")
    node13 = Node("I")
    node14 = Node("J")

    node5.adj_list.append(node7)
    node6.adj_list.append(node5)
    node7.adj_list.append(node10)
    node7.adj_list.append(node13)
    node8.adj_list.append(node6)
    node8.adj_list.append(node14)
    node9.adj_list.append(node5)
    node10.adj_list.append(node9)
    node11.adj_list.append(node12)
    node11.adj_list.append(node6)
    node12.adj_list.append(node13)
    node13.adj_list.append(node5)
    node14.adj_list.append(node11)

    bfs = BFS()
    bfs.print_nodes(bfs.BFS(node5))