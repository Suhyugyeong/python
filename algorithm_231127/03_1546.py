import sys

N = int(sys.stdin.readline())
scores = [int(i) for i in sys.stdin.readline().split()]
M = max(scores)
new_scores = [i / M * 100 for i in scores]

print(sum(new_scores)/N)

# n = int(input())
# m = list(map(int, input().split()))
# max_m = max(m)
# sum = 0
# for i in m:
#     print(i)
#     sum += i
# print(sum*100/max_m/n)