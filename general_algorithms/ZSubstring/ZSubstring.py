

class Z_Substring:
    def __init__(self, pattern, text):
        self.pattern = pattern
        self.text = text
        self.combined_text = self.pattern + self.text
        self.z_table = [0 for _ in range(len(self.combined_text))]


    def search(self):
        return

    def construct_z_table(self):
        size_pattern = len(self.pattern)
        size_text = len(self.text)
        size_combined = len(self.combined_text)
        # the first char has the value of the size of the text no matter what.
        self.z_table[0] = size_combined
        i = 0
        j = 1
        while j < size_combined and i < size_combined:
            k = j
            while k < size_combined:
                if self.combined_text[i] == self.combined_text[k]:
                    self.z_table[j] += 1
                    i += 1
                    print("char matched")
                    k += 1
                    if i == size_pattern:
                        print("found a match")
                else:
                    print("char doesn't match, reset i to 0")
                    i = 0
                    break
            j += 1


        return self.z_table