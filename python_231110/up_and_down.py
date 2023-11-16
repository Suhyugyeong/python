#random 모듈 사용
# from random import randint : 이런 식으로 모듈에서 특정함수만 가져올 수 있음..
import random

# 1부터 30까지 무작위로 숫자 선택
random_num = random.randint(1, 30)
#randint를 써서 정수만 뽑아내는 거고, 실수(float)를 뽑고 싶으면 random.uniform(1,30)을 사용하면 됨

while True:
    #while문의 조건은 항상 참 또는 거짓이어야 한다.
    #while문은 참이어야 실행되며, 무한루프를 조심해야 한다..
    user_input = int(input("숫자를 입력하세요.\n"))
    if user_input == random_num:
        print('정답입니다!!!')
        break # 정답인 경우에 무한반복이 종료!
    elif user_input > random_num:
        print("Down")
    else:
        print("UP")