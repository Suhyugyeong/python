# 구구단 for문
num = int(input())

for i in range(1, 9 + 1) :
    # print(num, "*", i, "=", num * i)
    # print("%d * %d = %d" % (num, i, num * i))
    print(f'{num} * {i} = {num * i}')