#40페이지에 자꾸만 0.0이 나옴..
n = int(input())
m = map(int, input().split())
# m에는 map객체가 저장되어 있고, 필요에 따라 list(m)과 같이 명시적으로 변환해야 한다.
# map 객체는 리스트와 유사하지만 실제로는 이터레이터이기 때문에 명시적으로 리스트로 변환해야 원하는 형태로 사용 가능..
max_m = max(m)
sum = 0
for i in m :
    sum += i
print(sum*100/max_m/n)

#강사님 추천! 리스트 컴프리헨션을 쓰자!
import sys
n = int(input())
m = [int(j) for j in sys.stdin.readline().split()]
max_m = max(m)
sum = 0
for i in m :
    sum += i
print(sum*100/max_m/n)

#gpt 해결안
#map 객체는 이터레이터(iterable)이기 때문에 한 번 이터레이션을 거치면서 내부의 데이터를 소비하게 됩니다. 
#즉, max(m)를 호출하면서 m을 한 번 순회하면서 최댓값을 찾은 후에는 다음에 나오는 for i in m에서는 m이 빈 상태가 됩니다. 
#그래서 두 번째 for 문에서는 m이 빈 상태이므로 아무 작업도 수행되지 않습니다.
#이 문제를 해결하려면, m을 리스트로 변환한 후에 최댓값을 찾아야 합니다. 
n = int(input())
m = list(map(int, input().split()))
max_m = max(m)
total_sum = sum(m)
result = total_sum * 100 / max_m / n
print(result)

#최대한 내 코드 살려서 ... list붙임으로써 해결!
n = int(input())
m = list(map(int, input().split()))
max_m = max(m)
sum = 0
for i in m :
    sum += i
print(sum*100/max_m/n)