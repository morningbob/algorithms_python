

class Bubble_Sort:
    def __init__(self, num_list):
        self.num_list = num_list


    def sort(self):
        # compare items one by one
        # swap to move bigger numbers to the end

        size_num_list = len(self.num_list)

        j = size_num_list

        while j > 0:
            i = 0
            while i + 1 < j:
                if self.num_list[i] > self.num_list[i+1]:
                    self.num_list[i], self.num_list[i+1] = self.num_list[i+1], self.num_list[i]
                i += 1
            j -= 1


    def print_num(self):
        for item in self.num_list:
            print(item, " ", end="")

