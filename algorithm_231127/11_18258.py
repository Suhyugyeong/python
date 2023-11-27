import sys
from collections import deque

N = int(sys.stdin.readline())
# queue = []
queue = deque()

# N 만큼 반복
for i in range(N):
    # 입력을 받아와서 공백으로 구분 -> 명령, *숫자 변수에 담는다. (명령은 문자열, 숫자는 리스트)
    cmd, *num = sys.stdin.readline().split()
    # 만약 명령이 push이면
    if cmd == 'push':
        # 숫자를 queue에 넣는다. (형변환 확인!)
        queue.append(int(num[0]))
    # 만약 명령이 pop이면
    elif cmd == 'pop':
        # queue가 비어있는 경우, -1 출력
        if not queue:
            print(-1)
        # queue가 들어있는 경우, 맨 앞의 데이터 꺼내서 출력
        else:
            # print(queue.pop(0))
            print(queue.popleft())
    # 만약 명령이 size이면
    elif cmd == 'size':
        # queue의 길이 출력
        print(len(queue))
    # 만약 명령이 empty이면
    elif cmd == 'empty':
        # queue가 비어있는 경우, 1 출력
        # queue가 들어있는 경우, 0 출력
        print(int(bool(not queue)))
    # 만약 명령이 front이면
    elif cmd == 'front':
        # queue가 비어있는 경우, -1 출력
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
        