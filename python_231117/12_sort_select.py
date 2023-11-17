def selection_sorted(list):
    for i in range(len(list)-1):
        min = i
        for j in range(i + 1, len(list)):
            if list[i] > list[j]:
                min = j
        list[i], list[min] = list[min], list[i] # 스왑
        # print(list)
    return list

chars = ['b', 'c', 'd', 'e', 'a']
print(selection_sorted(chars))