import sys

def up_and_down():
    import random
    random_num = random.randint(1, 30)

    while True:
        user_input = int(sys.stdin.readline())
        if user_input < 1 or user_input > 30:
            raise ValueError("원하는 숫자의 범위를 초과")
        if user_input == random_num:
            print('정답입니다!!!')
            break
        elif user_input > random_num:
            print("Down")
        else:
            print("UP")

try:
    up_and_down()
except Exception as e:
    print(e)