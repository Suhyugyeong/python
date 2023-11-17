def insertion_sorted(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1
        while j >= 0 and list[j] > key:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = key
    return list

chars = ['d', 'a', 'b', 'c', 'e']

print(insertion_sorted(chars))