# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from BellmanFord import Node, Edge, Bellman_Ford

if __name__ == '__main__':
    # we have to create the vertices
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")
    node6 = Node("F")
    node7 = Node("G")

    # let's create the edges
    edge1 = Edge(5, node1, node2)
    edge2 = Edge(9, node1, node5)
    edge3 = Edge(4, node2, node5)
    edge4 = Edge(12, node2, node3)
    edge5 = Edge(7, node2, node4)
    edge6 = Edge(3, node3, node4)
    edge7 = Edge(1, node3, node6)
    edge8 = Edge(9, node4, node7)
    edge9 = Edge(6, node5, node3)
    edge10 = Edge(4, node5, node6)
    edge11 = Edge(2, node6, node7)
    edge12 = Edge(6, node7, node3)

    # handle the adjacency lists
    node1.adj_list.append(edge1)
    node1.adj_list.append(edge2)
    node2.adj_list.append(edge3)
    node2.adj_list.append(edge4)
    node2.adj_list.append(edge5)
    node3.adj_list.append(edge6)
    node3.adj_list.append(edge7)
    node4.adj_list.append(edge8)
    node5.adj_list.append(edge9)
    node5.adj_list.append(edge10)
    node6.adj_list.append(edge11)
    node7.adj_list.append(edge12)

    # run the algorithm
    vertices = (node1, node2, node3, node4, node5, node6, node7)
    edges = (edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8, edge9, edge10, edge11, edge12)

    bf = Bellman_Ford(vertices, edges, node1)
    bf.Bellman_Ford()

    bf.get_shortest_path(node7)


