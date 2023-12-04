#주어진 자연수 N과 M에 대해 1부터 N까지의 숫자 중 중복허용하여 길이가 M인 수열을 찾아내는 깊이 우선 탐색(DFS)알고리즘


import sys
N, M = [int(i) for i in sys.stdin.readline().split()]
nums = [i for i in range(1, N + 1)]

# import itertools
# results = list(itertools.product(nums, repeat=M))
# for i in results:
#     print(*i)
# itertools.product를 사용하여 nums리스트의 요소들 중복을 허용하여 길이가 M인 조합을 생성하고 출력
# itertools모듈의 product함수를 사용, repeat = M 은 nums리스트의 각 원소를 M번 반복하여 모든 조합을 생성한다..
# M은 최종적으로 생성되는 각 조합의 길이, N은 원소의 개수
# repeat는 iterable에서의 반복횟수가 아니라, 전체 조합의 길이를 결정
# 각 iterable에서의 원소가 M번 반복되므로, 최종적인 각 조합의 길이가 M이 된다..

def dfs(path):
    if len(path) == M:
        print(*path)
        return
    for i in nums:
        path.append(i)
        dfs(path)
        path.pop()
dfs([])
