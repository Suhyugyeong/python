import sys

pipe = sys.stdin.readline().rstrip() # ()((()()))(()(()))
stack = []
result = 0

for i in range(len(pipe)):
    # 여는 괄호를 만나면 스택에 ( 를 추가
    if pipe[i] == '(':
        stack.append('(')
    # 닫는 괄호를 만나면, stack.pop()
    else:
        stack.pop()
        # 만약 닫는 괄호 앞에가 여는 괄호라면 (레이저!) -> result에 스택의 길이를 더해준다.
        if pipe[i-1] == '(':
            result += len(stack)
        # 만약 닫는 괄호 앞에가 닫는 괄호라면 (막대기의 끝) -> result에 1을 더해준다.
        else:
            result += 1
print(result)
