# 입력값 받아오기!
# 1) ??? 임포트
import sys

# 2) expr = 입력값 배열 [엔터까지 제외시키기] & -를 기준으로 분해
expr = list(map(str, sys.stdin.readline().strip().split('-')))
# expr = sys.stdin.readline().rstrip().split('-')

# 3) 최소값(min_result) 초기화
min_result = 0
for i in expr[0:1]:
    for j in i.split('+'):
        min_result += int(j)

for i in expr[1:]:
    for j in i.split('+'):
        min_result -= int(j)

print(min_result)