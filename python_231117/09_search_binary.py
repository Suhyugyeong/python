def find_my_num(list, value):
    
    start, end = 0, len(list)-1
    while start <= end:
        mid = (start + end) // 2
        if value < list[mid]:
            end = mid - 1
        elif value > list[mid]:
            start = mid + 1
        else:
            return mid
    return -1

print(find_my_num([1,2,3,4,5,6,7,8], 5))