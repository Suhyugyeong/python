# 입력값 받아오기!
# 1) ??? 임포트
import sys

# 2) expr = 입력값 배열 [엔터까지 제외시키기] & -를 기준으로 분해
expr = list(map(str, sys.stdin.readline().strip().split('-')))
# expr = sys.stdin.readline().rstrip().split('-')

# 3) 최소값(min_result) 초기화
min_result = 0
for i in expr[0:1]:
    #수식의 첫 번째 요소를 의미
    #이 부분은 '-'로 나뉘어진 수식 중에서 첫 번째인 덧셈 부분
    for j in i.split('+'):
        #첫 번째 요소를 '+'로 나뉘어진 부분으로 분리하고, 이를 반복하여 숫자들을 얻음
        min_result += int(j)
        #분리된 각 숫자를 정수로 변환하여 최종 결과에 더함
for i in expr[1:]:
    #수식의 두 번째 요소부터 마지막 요소까지를 의미
    # 이 부분은 '-'로 나뉘어진 수식 중에서 두 번째 이후의 뺄셈 부분
    for j in i.split('+'):
        min_result -= int(j)

print(min_result)