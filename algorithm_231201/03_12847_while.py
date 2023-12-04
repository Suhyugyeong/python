#길이가 N인 배열 pay에 연속된 m개의 원소를 선택하여 그 합이 최대가 되는 부분배열의 합을 구하기!
#슬라이딩 윈도우 기법을 사용

import sys
N, m = [int(i) for i in sys.stdin.readline().split()]
#N은 배열의 길이, m은 연속된 원소의 개수
pay = [int(i) for i in sys.stdin.readline().split()]
#배열 pay

start = 0
sum = sum(pay[:m])
max_sum = sum #최대합을 나타내는 변수를 초기화

while m < N:
    sum += pay[m] - pay[start]
    #현재 부분배열의 합에서 맨 앞의 원소를 빼고, 새로운 원소를 더하여 부분배열의 합을 업데이트
    max_sum = max(max_sum, sum)
    #현재까지의 최대 합(첫 m개의 원소로 이루어진 배열의 합) 과 
    #현재 부분배열의 합 중에서 더 큰 값을 max_sum에 저장
    start += 1 #부분배열의 시작을 오른쪽으로 한칸 이동..
    m += 1 #부분배열의 끝을 오른쪽으로 한 칸 이동..
print(max_sum)