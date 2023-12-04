def divide_conquer_product(start, end):
    if end == start:
        return start
    if end == start + 1:
        return start * end
    else:
        half = (start + end) // 2
        return divide_conquer_product(start, half) * divide_conquer_product(half + 1, end)
    
print(divide_conquer_product(1, 15))