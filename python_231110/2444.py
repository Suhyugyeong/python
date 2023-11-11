for i in range(number != 0):

#숫자 입력받기
number = int(input())
#조건 : *이 1부터 10까지 숫자 중 홀수만(%2==1) 
#그러면서 *이 중앙정렬이 되어야 하는데 총 줄의 개수는 9개
f'{"*":^9}'
#최대칸의 개수도 9개로 양쪽에 공백이 있어야 함
#실행문 한번 돌고나서 \n 개행해주기
#파이썬에서 print 함수는 기본적으로 출력이 끝난 후 자동으로 개행(newline)을 추가합니다. 



# 숫자를 입력 받음
number = int(input("숫자를 입력하세요: "))

# 입력값이 0 이상 10 이하이면서 홀수인지 확인
if 0 <= number <= 10 and number % 2 == 1:
    print(f"{number}은(는) 0 이상 10 이하이면서 홀수입니다.")
else:
    print(f"{number}은(는) 0 이상 10 이하이면서 홀수가 아닙니다.")


# 숫자를 입력 받음
n = int(input("숫자를 입력하세요: "))

# 별 찍기
for i in range(1, n + 1):
    print('*' * i)


    """# 높이를 입력 받음
height = int(input("피라미드의 높이를 입력하세요: "))

# 피라미드 출력
for i in range(1, height + 1):
    spaces = ' ' * (height - i)
    stars = '*' * (2 * i - 1)
    print(spaces + stars)

    """
    
    """# 마름모의 높이를 입력 받음
height = int(input("마름모의 높이를 입력하세요: "))

# 위쪽 부분 출력
for i in range(1, height + 1):
    spaces = ' ' * (height - i)
    stars = '*' * (2 * i - 1)
    print(spaces + stars)

# 아래쪽 부분 출력
for i in range(height - 1, 0, -1):
    spaces = ' ' * (height - i)
    stars = '*' * (2 * i - 1)
    print(spaces + stars)

    """