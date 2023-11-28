#https://www.acmicpc.net/problem/2953
#다섯 명의 요리사, 다섯 개의 음식
import sys

def i_am_cook():
    sum_scores = []
    for _ in range(5):
        score = [int(i) for i in sys.stdin.readline().split()]
        #각 요리사가 만든 5개 음식에 대한 점수
        sum_scores.append(sum(score))
        #score를 sum내장함수로 더해서 sum_sores 리스트에 추가
    print(sum_scores.index(max(sum_scores)) + 1, max(sum_scores))
    #index 메서드를 사용해서 최대값의 인덱스 찾고 인덱스는 0부터 시작하니께 1 더해 몇 번째 사람인지..
    
i_am_cook()

    # sum_scores = [sum([int(i) for i in sys.stdin.readline().split()]) for _ in range(5)]