
class Insertion_Sort:
    def __init__(self, num_list):
        self.num_list = num_list


    def sort(self):
        size_num_list = len(self.num_list)

        for i in range(1, size_num_list):
            print("one loop")
            target = self.num_list[i]
            for j in range(i, 0, -1):
                print("ran")
                print("target", target)
                if self.num_list[j-1] > target:
                    print("j-1", self.num_list[j-1], ">", "target", target)
                    print("j-1", j-1)
                    self.num_list[j] = self.num_list[j-1]
                    self.num_list[j-1] = target
                    self.print_num()
                else:
                    print("j-1", self.num_list[j-1], "<", "target", target)
                    print("j-1", j-1)
                    self.num_list[j] = target
                    self.print_num()
                    break


    def swap(self, index_1, index_2):
        print("swap", self.num_list[index_1], self.num_list[index_2])
        self.num_list[index_1], self.num_list[index_2] = \
            self.num_list[index_2], self.num_list[index_1]

    def print_num(self):
        for item in self.num_list:
            print(item, " ", end="")