def robot(calc_func):
    print("삐리리-삐빅! 로봇계산기입니다.")
    num1 = int(input("첫번째 숫자를 입력하세요"))
    num2 = int(input("두번째 숫자를 입력하세요"))
    print("치지직.. 삐빅!!! 삐빅!!!")
    result = calc_func(num1, num2)
    print("휴... 계산 결과는요...")
    print(f"{result} 입니다. 삐빅삐빅!")
    
def plus(a, b):
    return a + b
def minus(a, b):
    return a - b

robot(plus)
robot(minus)