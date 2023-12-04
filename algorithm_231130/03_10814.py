#사용자로부터 입력받은 나이와 이름을 저장, 나이 기준 오름차순 정렬
import sys

N = int(sys.stdin.readline()) # 몇 명?
# saram = []
# for i in range(N):
#     age, name = sys.stdin.readline().split()
#     saram.append([age, name])
saram = [sys.stdin.readline().split() for _ in range(N)] #각 사람의 나이와 이름을 2차원 리스트에 저장
#2차원 리스트란 리스트 안에 또 다른 리스트가 포함 된 형태
#예 saram = [["10", "min"], ["20", "jung"]]

saram.sort(key=lambda x:int(x[0]))

for i in saram:
    print(*i) #리스트 i의 각 요소를 공백으로 구분하여 출력(*은 언패킹)