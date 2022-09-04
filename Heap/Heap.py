CAPACTIY = 10


# maximum heap
class Heap:
    def __init__(self):
        self.heap_pointer = 0
        self.heap = CAPACTIY * [0]

    def insert(self, data):
        # check if the heap is full
        if self.heap_pointer >= CAPACTIY:
            print("insert", "heap is full")
            return
        print("inserted data", data)
        self.heap[self.heap_pointer] = data
        self.heap_pointer += 1
        self.check_validity_bottom_up(self.heap_pointer - 1)

    # this method checks if the heap is valid,
    # that is, the parent is greater than the children
    def heapify_to_parent(self, index):
        parent_index = (index - 1) // 2
        # that the parent node is smaller
        if self.heap[index] > self.heap[parent_index]:
            # switch the data
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]

    # it checks the node recursively until it reaches the root
    def check_validity_bottom_up(self, index):
        while index < len(self.heap) and index > 0:
            print("checking validity", "index", index)
            self.heapify_to_parent(index)
            parent_index = (index - 1) // 2
            index = parent_index


    # we can keep track of the largest index, which is the index where the greatest item is
    def heapify_to_child(self, index):
        left_child_index = index * 2 + 1
        right_child_index = index * 2 + 2
        largest_index = index
        if index < self.heap_pointer and index >= 0:
            # find the max child to swap
            if left_child_index < self.heap_pointer and self.heap[left_child_index] > self.heap[right_child_index] and \
                    self.heap[index] < self.heap[left_child_index]:
                largest_index = left_child_index
                # swap with left child
                print("heapify to child", "left child is greater", self.heap[left_child_index])
                self.heap[index], self.heap[left_child_index] = self.heap[left_child_index], self.heap[index]
            if right_child_index < self.heap_pointer and self.heap[right_child_index] > self.heap[left_child_index] and \
                    self.heap[index] < self.heap[right_child_index]:
                largest_index = right_child_index
                # swap with right child
                print("heapify to child", "right child is greater", self.heap[right_child_index])
                self.heap[index], self.heap[right_child_index] = self.heap[right_child_index], self.heap[index]
            # if the index doesn't change, we stop the recursion
            if largest_index == index:
                return None
            else:
                return largest_index
        return None

    def check_validity_top_down(self, index):
        largest_index = index
        # check if the children of the node is greater than the parent
        while largest_index != None:
            print("checking validity", "largest index", largest_index)
            #self.print_heap()
            largest_index = self.heapify_to_child(largest_index)



    # this method first switch the data in the root with the data in the last cell
    # it returns the data of the root first
    def pop(self):
        root = self.heap[0]
        # swap
        self.heap[0], self.heap[self.heap_pointer - 1] = self.heap[self.heap_pointer - 1], self.heap[0]
        # update heap pointer to the end of the occupied item in the heap
        self.heap_pointer -= 1
        # after the switch, we need to make sure it is still a valid heap.
        self.check_validity_top_down(0)
        return root

    def sort_descending(self):
        for i in range(self.heap_pointer):
            print(self.pop(), " ", end="")

    def print_heap(self):
        for item in self.heap:
            print(item, " ", end="")



