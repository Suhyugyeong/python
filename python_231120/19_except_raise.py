import sys

def up_and_down():
    import random
    random_num = random.randint(1, 30)
    #정수만 만들거니께 randint

    while True:
        user_input = int(sys.stdin.readline())
        if user_input < 1 or user_input > 30:
            raise ValueError("원하는 숫자의 범위를 초과")
        #예외 상황에 대응
        #제대로 입력을 끝까지 받아내겠다는 의지..
        if user_input == random_num:
            print('정답입니다!!!')
            break
        elif user_input > random_num:
            print("Down")
        else:
            print("UP")

try:
    #예외가 발생하지 않으면 try 블록의 코드 정상적 실행, 예외 발생하면 비정상적으로 종료되는 대신 예외 처리 부분이 처리 됨.
    #일부러 ValueError를 발생시키는데 try문 없으면 이 예외를 처리하지 않고 프로그램이 종료되는 문제가 생김..
    #while문과 함께 사용하여 예외 처리 후에도 while루프가 계속해서 동작할 수 있도록 구성
    #반복적으로 사용자에게 입력을 받아 처리하거나 특정 조건이 충족될 때까지 반복하는 상황에서 유리
    up_and_down()
except Exception as e:
    print(e)