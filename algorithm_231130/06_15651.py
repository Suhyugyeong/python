# 자연수 N , M -> 3 1
# nums = [1, 2, ..., N]
# M : 수열 길이

import sys
N, M = [int(i) for i in sys.stdin.readline().split()]
nums = [i for i in range(1, N + 1)]

# import itertools
# results = list(itertools.product(nums, repeat=M))
# for i in results:
#     print(*i)

def dfs(path):
    if len(path) == M:
        print(*path)
        return
    for i in nums:
        path.append(i)
        dfs(path)
        path.pop()
dfs([])
