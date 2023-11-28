import sys

N = int(sys.stdin.readline())
queue = [i for i in range(1, N + 1)]

# for i in range(N-1):
while len(queue) != 1:
    queue.pop(0)
    queue.append(queue.pop(0))
print(*queue)