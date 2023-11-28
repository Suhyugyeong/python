#https://www.acmicpc.net/problem/18258

import sys
from collections import deque
#collections모듈에서 제공하는 deque를 사용하여 queue를 구현
#double-ended queue의 약자로, 양쪽 끝에서 데이터를 추가하거나 제거할 수 있는 자료구조
N = int(sys.stdin.readline())
queue = deque()
#빈 큐를 생성
#queue = []
#리스트는 큐의 연산을 수행하기에 적절하지 않을 수 있다..

# N 만큼 반복
for i in range(N):
    #(명령은 문자열, 숫자는 리스트)
    cmd, *num = sys.stdin.readline().split()
    if cmd == 'push':
        # 숫자를 queue에 넣는다. (형변환 확인!)
        queue.append(int(num[0]))
    elif cmd == 'pop':
        # queue가 비어있는 경우, -1 출력
        if not queue:
            print(-1)
        # queue가 들어있는 경우, 맨 앞의 데이터 꺼내서 출력
        else:
            # print(queue.pop(0))
            print(queue.popleft())
            #시간복잡도는 후자가 유리
    elif cmd == 'size':
        print(len(queue))
    elif cmd == 'empty':
        # queue가 비어있는 경우, 1 출력
        # queue가 들어있는 경우, 0 출력
        print(int(bool(not queue)))
    elif cmd == 'front':
        if not queue:
            print(-1)
        # queue가 들어있는 경우, queue의 0번째 출력
        else:
            print(queue[0])    
    # 만약 명령이 back이면
    else:
        # queue가 비어있는 경우, -1 출력
        if not queue:
            print(-1)
        # queue가 들어있는 경우, queue의 -1번째 출력
        else:
            print(queue[-1])   
        