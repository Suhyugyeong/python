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
            print(stack.pop())
        else:
            print(-1)
    elif cmd == 'size':
        print(len(stack))
    elif cmd == 'empty':
        print(int(bool(not stack)))
    elif cmd == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)