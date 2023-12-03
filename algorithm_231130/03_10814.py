import sys

N = int(sys.stdin.readline())
# saram = []
# for i in range(N):
#     age, name = sys.stdin.readline().split()
#     saram.append([age, name])
saram = [sys.stdin.readline().split() for _ in range(N)]

saram.sort(key=lambda x:int(x[0]))

for i in saram:
    print(*i)