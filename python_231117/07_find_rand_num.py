import random
import sys

with open("rand_num10.txt", "w", encoding = "utf-8") as f:
    for i in range(10):
        f.write(f"{random.randint(1,10)}\n")
#랜덤한 파일은 계속 바뀐다.

#사용자의 입력을 받아오고
number = int(sys.stdin.readline())
#단일한 정수값을 표준 입력에서 한 번 받아옴..
#input('') 속도 저하의 문제
#system 모듈 안에 stdin 표준입력 
#이걸 쓰려면 import sys를 해야합니다!!!!
#대량의 입력을 처리할 때 사용

#파일을 다시 읽어온다.
def find_num(num):
    with open("rand_num10.txt", "r", encoding="utf-8") as f:
        line_num = 0
        for i in f:
            line_num += 1
            if num == int(i):
                return line_num
        return -1

#사용자의 입력과 같은 숫자가 있다면, 그 해당 라인 번호 출력!
#사용자의 입력과 같은 숫자가 없다면, -1 출력(반환)

find_num(number)