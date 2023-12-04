#길이가 N인 배열 pay에서 길이가 M인 부분배열의 합 중에서 최댓값을 구하는 코드
#슬라이딩 윈도우 기법

import sys

N, M = [int(i) for i in sys.stdin.readline().split()] # 5 3
pay = [int(i) for i in sys.stdin.readline().split()] # 10 20 30 20 10

window = sum(pay[:M]) #60
max_pay = window
for i in range(N - M): #반복문을 사용하여 배열을 한 칸씩 오른쪽으로 이동하면서 부분배열의 합을 계산
    window += pay[i+M]-pay[i] 
    # 새로 추가된 원소와 제거된 원소를 이용하여 부분배열의 합을 업데이트
    max_pay = max(max_pay, window) 
    # 현재까지의 최대 부분배열의 합과 현재 부분배열의 합 중에서 큰 값을 선택하여 max_pay에 저장

# window1 = sum(pay[0:3])
# window1 += pay[3] - pay[0] 
# window1 += pay[4] - pay[1]

print(max_pay)