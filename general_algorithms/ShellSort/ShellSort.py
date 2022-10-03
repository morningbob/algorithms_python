
class Shell_Sort:
    def __init__(self, num_list):
        self.num_list = num_list


    def sort(self):
        # divide list to partitions
        # sort the nums apart some space along the list
        gap = len(self.num_list) // 2

        while gap > 0:
            for i in range(gap, len(self.num_list), gap):
                print("one loop")
                target = self.num_list[i]
                for j in range(i, 0, -gap):
                    if self.num_list[j-gap] > target:
                        print("j-gap", self.num_list[j - gap], ">", "target", target)
                        print("j-gap", j - gap)
                        self.num_list[j] = self.num_list[j-gap]
                        self.num_list[j-gap] = target
                        self.print_num()
                    else:
                        print("j-gap", self.num_list[j - gap], "<", "target", target)
                        print("j-gap", j - gap)
                        self.num_list[j] = target
                        self.print_num()
                        break
            gap = gap // 2


    def print_num(self):
        for item in self.num_list:
            print(item, " ", end="")


