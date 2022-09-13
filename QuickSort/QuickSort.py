

class Quick_Sort:
    def __init__(self, num_list):
        self.num_list = num_list
        self.sort(0, len(self.num_list) - 1)


    def sort(self, low, high):
        if low >= high:
            return

        pivot_index = self.partition(low, high)
        # so the pivot index is in it's correct place
        # we don't move it or process it
        self.sort(low, pivot_index - 1)
        self.sort(pivot_index + 1, high)

    def partition(self, low, high):
        pivot_index = (low + high) // 2

        # swap pivot with high index item, then we can do the comparisons
        self.swap(pivot_index, high)

        i = low
        for j in range(low, high):
            if self.num_list[j] < self.num_list[high]:
                self.swap(j, i)
                i += 1

        # swap pivot to the correct place in the middle
        self.swap(i, high)

        # return the pivot index
        # so we can use the pivot to indicate the start and end of the smaller partition
        return i

    def swap(self, index_1, index_2):
        self.num_list[index_1], self.num_list[index_2] = \
            self.num_list[index_2], self.num_list[index_1]

    def print_num(self):
        for item in self.num_list:
            print(item, " ", end="")