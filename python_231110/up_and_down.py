import random

# 1부터 30까지 무작위로 숫자 선택
random_num = random.randint(1, 30)

while True:
    user_input = int(input("숫자를 입력하세요.\n"))
    
    if user_input == random_num:
        print('정답입니다!!!')
        break # 정답인 경우에 무한반복이 종료!
    elif user_input > random_num:
        print("Down")
    else:
        print("UP")