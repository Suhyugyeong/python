import sys
from collections import defaultdict

TEST_CASE  = int(sys.stdin.readline()) # 2

for i in range(TEST_CASE):
    N = int(sys.stdin.readline())
    wear_dict = defaultdict(list)
    for j in range(N):
        item, cate = sys.stdin.readline().split()
        wear_dict[cate].append(item)
    result = 1
    for k in wear_dict:
        result *= len(wear_dict[k]) + 1
    result -= 1
    print(result)