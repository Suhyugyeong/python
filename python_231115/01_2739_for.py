# 구구단 for문
dan_num = int(input())

for j in range(1, 9 + 1) :
    print(dan_num, "*", j, "=", dan_num * j)
    print("%d * %d = %d" % (dan_num, j, dan_num * j))
    print(f'{dan_num} * {j} = {dan_num * j}')