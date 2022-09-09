
class Rabin_Karp:
    def __init__(self, pattern, text):
        self.pattern = pattern
        self.text = text
        self.alphabet_size = 26
        self.prime_number = 31

    def search(self):
        # first we hash the pattern
        # we use ord to get the numeric representation of the character
        # then we hash the strings that has the length of the pattern
        # we subtract the hash of the first letter and add the hash of the last
        # letter while calculating the hash of subsequent strings
        # we store the hashes value in an array

        hash_pattern = 0
        size_pattern = len(self.pattern)
        hash_text = []
        size_text = len(self.text)
        result = []

        for i in range(size_pattern):
            hash_pattern += ord(self.pattern[i]) * self.alphabet_size ** (size_pattern - i - 1)
            print("size of pattern", size_pattern - i - 1)

        #hash_pattern = hash_pattern % self.prime_number
        print("hash", hash_pattern)


        current_hash_text = self.hash_strings(size_pattern, self.text)
        print("hash of text", current_hash_text)
        print("first phrase after %", current_hash_text % self.prime_number)
        if hash_pattern % self.prime_number == current_hash_text % self.prime_number:
            print("found a match")
            result.append(0)

        hash_text.append(current_hash_text)

        for i in range(1, size_text):
            print("old char", self.text[i-1])
            old_char = self.text[i-1]

            if (i + 3) < size_text:
                new_char = self.text[i+3]
                print("i", i, "i+3", i+3)
                print("new char", self.text[i + 3])
                print("new phrase", self.text[i:i+4])
                new_hash = self.rolling_hash(current_hash_text, old_char, new_char,
                                             size_pattern)
                print("new hash", new_hash)
                current_hash_text = new_hash
                # compare to the hash of the pattern
                print("new hash after %", current_hash_text % self.prime_number)
                if (hash_pattern % self.prime_number == current_hash_text % self.prime_number):
                    # because hash function is not perfect
                    # we need to compare the strings
                    print("text phrase", self.text[i:i+4])
                    if (self.pattern == self.text[i:i+4]):
                        print("found a match")
                        print("i", i)
                        result.append(i)

                hash_text.append(new_hash)
            else:
                break

        return result


    def hash_strings(self, size, string):
        hash_value = 0
        for i in range(size):
            hash_value += ord(string[i]) * self.alphabet_size ** (size - i - 1)
        print("raw hash", hash_value)

        return hash_value

    def rolling_hash(self, previous_hash, old_char, new_char, size_pattern):
        print("previous hash", previous_hash)
        print("old char", old_char)
        print("new char", new_char)
        hash = (abs(previous_hash - (ord(old_char) * (self.alphabet_size ** (size_pattern - 1))))
                * self.alphabet_size + ord(new_char) * self.alphabet_size)
        print("raw hash", hash)

        #hash = hash % self.prime_number
        #if hash < 0:
        #    hash = hash + self.prime_number
        return hash



