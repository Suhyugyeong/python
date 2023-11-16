# 팩토리얼 (factorial)
import sys

def factorial(num):
    if num == 0:
        return 1
    result = factorial(num - 1)
    return num * result

number = int(sys.stdin.readline())
print(factorial(number))