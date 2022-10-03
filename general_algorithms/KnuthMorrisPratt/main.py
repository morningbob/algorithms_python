from KnuthMorrisPratt import Knuth_Morris_Pratt

if __name__ == '__main__':

    kmp = Knuth_Morris_Pratt('aab', 'aacaabaab')
    kmp.search()

    kmp = Knuth_Morris_Pratt('aab', 'aabaabaab')
    kmp.search()