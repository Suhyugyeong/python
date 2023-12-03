import sys
N = int(sys.stdin.readline())

arr = []
for _ in range(N):
    X = int(sys.stdin.readline())
    if X == 0:
        if len(arr) == 0:
            print(0)
        else:
            print(min(arr))
            arr.remove(min(arr))
    else:
        arr.append(X)