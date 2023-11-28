import sys

K = int(sys.stdin.readline())
stack = []
#일반적으로 파이썬은 리스트를 사용하여 스택을 구현
#후입선출 구조!!

for i in range(K):
    num = int(sys.stdin.readline())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)
        #새로운 원소가 스택의 맨 위로 올라감

print(sum(stack))