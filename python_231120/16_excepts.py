import sys
def hundred_divisor():
    try:
        print("100의 약수를 입력하세요")
        num = int(sys.stdin.readline().rstrip())
        if 100 % num == 0:
            print('약수가 맞습니다.')
        else:
            print('틀렸습니다.')
    except ZeroDivisionError as e:
        print("0으로 나눌 수는 없어요.", e)
        hundred_divisor()
    except ValueError as e:
        print("정수 값을 입력하지 않아 프로그램을 종료합니다.", e)
    except Exception as e:
        print("알 수 없는 에러", e)
hundred_divisor()