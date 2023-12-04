#최소 힙(Min Heap) 활용하여 0이 입력되면 최소값을 출력, 0이 아닌 경우 배열에 값을 추가

# 첫째줄에 연산의 개수 n이 주어진다.
# 그 이후에 연산 정보 x가 자연수로 주어지면 배열에 자연수 x를 넣는다.

# x가 0이면 배열에서 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다.
# 배열에 값이 없으면 0을 출력한다.

# 프로그램은 처음에 비어있는 배열에서 시작하게 된다.

import sys
import heapq
# heapq 모듈은 heap자료 구조를 제공
N = int(sys.stdin.readline())
arr = []
#힙 자료구조를 저장할 리스트 초기화
for _ in range(N):
    #N개의 연산을 입력받을 것
    X = int(sys.stdin.readline())
    if X == 0:
        if len(arr) == 0:
            #배열이 비어있는 경우
            print(0)
        else:
            print(heapq.heappop(arr))
            #배열이 비어있지 않는 경우, heapq모듈의 headppop함수를 사용하여 힙에서 최소값을 꺼내어 출력
    else:
        # 배열에 값 넣기
        #힙 자료구조 특성에 따라 추가된 값은 최소 힙의 규칙을 지켜가며 정렬됨
        heapq.heappush(arr, X)
        

#힙은 일반적으로 최소 힙이며, 최소값은 항상 루트 노드에 위치하게 됨