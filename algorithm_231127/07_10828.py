#스택 자료 구조를 구현하는 코드
import sys

N = int(sys.stdin.readline())
stack = []

for i in range(N):
    cmd, *num = sys.stdin.readline().split()
    if cmd == "push":
        num = int(num[0])
        stack.append(num)
    elif cmd == 'pop':
        if stack:
            #스택이 비어있지 않은 경우,
            print(stack.pop())
        else:
            print(-1)
    elif cmd == 'size':
        print(len(stack))
    elif cmd == 'empty':
        print(int(bool(not stack)))
        #not stack 스택이 비어있을 때 True
        #스택이 비어있으면 not stack은 True, 비어있지 않으면 False
        #bool값으로 True는 1, False는 0으로 변환
    elif cmd == 'top':
        #스택의 가장 위에 있는 값을 출력
        if stack:
            print(stack[-1])
        else:
            print(-1)