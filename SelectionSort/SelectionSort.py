
class Selection_Sort:
    def __init__(self, num_list):
        self.num_list = num_list


    def sort(self):
        size_num_list = len(self.num_list)
        # find the min item and move to the left most
        j = 0
        while j < size_num_list:
            min_num_index = j
            i = j
            while i < size_num_list:
                if self.num_list[i] < self.num_list[min_num_index]:
                    min_num_index = i
                i += 1

            if min_num_index != j:
                self.swap(min_num_index, j)

            j += 1


    def swap(self, index_1, index_2):
        print("swap", self.num_list[index_1], "with", self.num_list[index_2])
        self.num_list[index_1], self.num_list[index_2] = \
            self.num_list[index_2], self.num_list[index_1]

    def print_num(self):
        for item in self.num_list:
            print(item, " ", end="")

