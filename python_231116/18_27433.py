# 팩토리얼 (factorial)/ 재귀함수 사용
import sys

def factorial(num):
    if num == 0:
        return 1
    #종료조건
    result = factorial(num - 1)
    #자기자신을 다시 호출한다!!
    #메모리에 스택이 쌓임..
    return num * result
    
number = int(sys.stdin.readline())
print(factorial(number))

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)

# result = factorial(5)
# print(result) 