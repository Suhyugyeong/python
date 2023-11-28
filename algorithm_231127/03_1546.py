import sys

N = int(sys.stdin.readline())
scores = [int(i) for i in sys.stdin.readline().split()]
M = max(scores)
#정규화를 위한 기준값으로 사용하기 위해 최대값 뽑아내고..
new_scores = [i / M * 100 for i in scores]
#순서 중요! 리스트 컴프리헨션!
print(sum(new_scores)/N)



#내가 map으로 했을 때 0.0으로 답이 나왔음.. 그걸 해결하기 위해 list에 담아줘야함..
#map함수는 그 결과를 이터레이터로 반환하지만 이터레이터와 리스트는 유사하나 같지 않다!!!
# n = int(input())
# m = list(map(int, input().split()))
# max_m = max(m)
# sum = 0
# for i in m:
#     print(i)
#     sum += i
# print(sum*100/max_m/n)