from SelectionSort import Selection_Sort

if __name__ == '__main__':
    n = [45, 100, 0, 1, -5, -10, 4, 5, 6, 13]
    selection = Selection_Sort(n)
    selection.sort()

    selection.print_num()

