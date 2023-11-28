import sys
from collections import Counter

TEST_CASE  = int(sys.stdin.readline())

for i in range(TEST_CASE):
    N = int(sys.stdin.readline())
    wear = []
    for j in range(N):
        item, cate = sys.stdin.readline().split()
        wear.append(cate)
    wear_Counter = Counter(wear)
    result = 1
    for k in wear_Counter:
        result *= wear_Counter[k] + 1
    result -= 1
    print(result)