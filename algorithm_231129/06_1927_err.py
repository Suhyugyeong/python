#작동은 하나, 개선할 여지가 있다.. 비효율적

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
            #min(arr)를 호출하면서 리스트를 매번 탐색하게 되고, 비효율적임
            arr.remove(min(arr))
            #최소값을 찾은 후에 해당 리스트에서 제거하는 과정으로 최소값을 찾는 것과 제거하는 것, 동일한 연산을 두 번이나 함!!
            #이걸 개선하기 위해 heapq모듈을 사용해 최소 힙을 유지하면서 작업하는 것이 효율적..
    else:
        arr.append(X)