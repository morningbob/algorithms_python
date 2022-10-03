
class Knuth_Morris_Pratt:
    def __init__(self, pattern, text):
        self.pattern = pattern
        self.text = text
        self.pi_table = [0] * len(self.pattern)
        self.construct_pi_table()

    # we loop through the text char by char exactly once
    # we increment i and j if there is a match
    # if there is a mismatch, we look up the j-1 value from the pi table
    # and move j pointer to the index
    def search(self):
        size_pattern = len(self.pattern)
        size_text = len(self.text)
        result = []
        i = 0
        j = 0
        while i < size_text:
            while j < size_pattern and i < size_text:
                if self.pattern[j] == self.text[i]:
                    # we increment i and j
                    if j < size_pattern:
                        j += 1
                        print("j incremented", j)
                        if j == size_pattern:
                            print("found a match at ", i-j+1)
                            result.append(i-j+1)
                            j = 0
                    i += 1
                    print("i incremented", i)

                else:
                    # j move the j-1 position in the pi table
                    j = self.pi_table[j-1]
                    print("j repositioned", j)
                    # we don't change i here unless j = 0
                    if j == 0:
                        i += 1





    def construct_pi_table(self):
        size_pattern = len(self.pattern)
        # the first value is 0 no matter what
        self.pi_table[0] = 0
        # compare the first char with the second char
        # if they match, record the value 1, if not record 0
        # we loop through the rest of the pattern
        for i in range(1, size_pattern):
            print("i", i)
            value = 0
            k = i
            for j in range(k, size_pattern):
                print("j", j, "k", k)
                if self.pattern[k-1] == self.pattern[j]:
                    value += 1
                    k += 1
                else:
                    break

            self.pi_table[i] = value
            print("pi table value", value)
