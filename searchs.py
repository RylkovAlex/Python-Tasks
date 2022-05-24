def binary_search(list_, el):
    l = [*list_]
    index = 0
    while len(l) >= 1:
        length = len(l)
        middle = length // 2

        if el == l[middle]:
            print('Result', list_[middle + index])
            print('Position', middle + index)
            return middle + index
        elif length == 1:
            print('No element')
            return False
        elif (l[middle] > el):
            l = l[:middle]
        else:
            index += middle
            l = l[middle::]