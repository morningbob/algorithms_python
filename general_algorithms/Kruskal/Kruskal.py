
class Edge:
    def __init__(self, weight, start_vertex, end_vertex):
        self.weight = weight
        self.start_vertex = start_vertex
        self.end_vertex = end_vertex

    def __lt__(self, other):
        return self.weight < other.weight

class Vertex:
    def __init__(self, name):
        self.node = None
        self.name = name


class Node:
    def __init__(self, node_id, parent=None):
        self.id = node_id
        self.parent = parent
        self.rank = 0

class Disjoint_Set:
    def __init__(self, vertex_list):
        self.vertex_list = vertex_list
        self.root_nodes = []
        self.make_sets()
        self.print_nodes()

    # this method create the nodes as distinct entities at the beginning
    # one node for every vertex
    def make_sets(self):
        for vertex in self.vertex_list:
            vertex.node = Node(len(self.root_nodes))
            self.root_nodes.append(vertex.node)

    def find(self, child_node):

        node = child_node
        current_node = child_node
        if node.parent is not None:
            print("node", node.id, "parent", node.parent.id)
            node = node.parent

        root = node
        # path compression, that next time when the current node is accessed
        # O(1)
        current_node.parent = root
        return root.id




    # it join the two distinct sets into one set,
    # lower rank tree will be attached under higher rank tree
    def union(self, node_1, node_2):
        # get the representative of node 1
        rep_1_id = self.find(node_1)
        # get the representative of node 2
        rep_2_id = self.find(node_2)

        # if the id is the same, that means they have the same root
        # they are in a set, we don't do the union
        if rep_1_id == rep_2_id:
            return

        rep_1 = self.root_nodes[rep_1_id]
        rep_2 = self.root_nodes[rep_2_id]


        if rep_1.rank > rep_2.rank:
            # attach 2 to 1
            rep_2.parent = rep_1
            # rep_1 is higher than rep_2, so the rank of rep_1 is not affected
        elif rep_1.rank < rep_2.rank:
            # attach 1 to 2
            rep_1.parent = rep_2

        elif rep_1.rank == rep_2.rank:
            rep_2.parent = rep_1
            rep_1.rank += 1
            # rep_1 is the same rank with rep_2
            # the rank should increase by one if rep_2 attached to it




# in Kruskal Algorithm, we use disjoint set as underlying data structure
# so, we modify the disjoint set inside
class Kruskal:
    def __init__(self, vertex_list, edge_list):
        self.vertex_list = vertex_list
        self.edge_list = edge_list

    def find_minimum_spanning_tree(self):
        # this stores the result of the edges needed for minimum spanning tree
        result = []
        # create a disjoint set for the data
        disjoint_set = Disjoint_Set(self.vertex_list)
        # sort the edges in ascending order, start with the lowest weight edge.
        self.edge_list = sorted(self.edge_list)

        # we find the rep of the 2 nodes to see if they are the same
        # the same means they are in the same set.
        # then, the edge can't be added
        # if they are different, we perform the union operation
        for edge in self.edge_list:
            u = edge.start_vertex
            v = edge.end_vertex
            print("edge", edge.start_vertex.name, edge.end_vertex.name)
            index_u = disjoint_set.find(u.node)
            index_v = disjoint_set.find(v.node)

            if index_u == index_v:
                print("same root", index_v)

            else:
                print("perform union")
                disjoint_set.union(u.node, v.node)

                # we add the edge to the result edges list
                result.append(edge)

        self.print_nodes(disjoint_set)
        return result

    def print_nodes(self, set):
        for node in set.root_nodes:
            print("node", node.id, "parent", node.parent.id)










