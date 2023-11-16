num = 3

def hanoi(value):
    if value == 1:
        return 1
    return 1 + (2 * hanoi(value-1))
    # first = hanoi(value-1)
    # second = 1
    # third = hanoi(value-1)
    # return first+second+third
    
print(hanoi(num))

def hanoi_detail(value, start, mid, end):
    if value == 1:
        print(start,end)
        return
    hanoi_detail(value-1, start, end, mid)
    print(start, end)
    hanoi_detail(value-1, mid, start, end)
    return
# print(2 ** num - 1)
hanoi_detail(num, 1, 2, 3)