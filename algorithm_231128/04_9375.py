import sys

TEST_CASE  = int(sys.stdin.readline()) # 2

for i in range(TEST_CASE):
    N = int(sys.stdin.readline())
    wear_dict = {}
    for j in range(N):
        item, cate = sys.stdin.readline().split()
        if cate in wear_dict:
            wear_dict[cate].append(item)
        else:
            wear_dict[cate]=[]
            wear_dict[cate].append(item)
    result = 1
    for k in wear_dict:
        result *= len(wear_dict[k]) + 1
    result -= 1
    print(result)