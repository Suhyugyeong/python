class Node:
    def __init__(self, data):
        #__init__ 파이썬의 특별한 메서드로, 초기화를 담당. 클래스의 인스턴스가 생성될 때 자동으로 호출되는 메서드
        self.data = data
        self.next = None
        #다음 노드를 가리키는 next 속성

class LinkedList:
    #단일 연결 리스트를 정의
    def __init__(self, value):
        #__int__메서드는 연결 리스트를 초기화
        #초기에 하나의 노드를 갖고 이 노드가 연결리스트의 시작
        self.head = Node(value)
        #head는 연결리스트의 시작점, 리스트의 맨 앞의 노드를 가리키는 포인터
    
    def insert(self, value):
        #새로운 노드를 연결 리스트에 추가
        current = self.head
        #현재 노드 current를 리스트의 끝까지 이동한 후 새로운 노드를 현재 노드의 next로 설정하여 추가
        while current.next is not None:
            #만약 현재노드의 다음노드가 None이 아니면 현재 노드를 다음노드로 이동..
            #이 과정을 현재 노드의 다음 노드가 None이 될 때까지 반복
            #즉, 현재 노드가 마지막 노드에 도달하면 루프를 종료
            current = current.next
        current.next = Node(value)
    
    def get_node(self, index):
        #주어진 인덱스에 해당하는 노드를 반환
        current = self.head
        count = 0
        while count < index:
            count += 1
            current = current.next
        return current
    
    def delete(self, index):
        #해당 노드를 삭제, 삭제된 노드의 데이터를 반환
        #만약 index가 0이ㅣ면 해당 노드를 삭제하고 새로운 헤드를 지정, 혹은 해당 인덱스 이전의 노드를 찾아 그 다음 노드를 가리키는 구조
        if index == 0:
            del_node = self.head.data
            self.head = self.head.next
            return del_node
        node = self.get_node(index - 1)
        del_node = node.next.data
        node.next = node.next.next
        return del_node


#조세푸스 문제를 해결하는 알고리즘
#n명의 사람이 원형으로 모여 앉아있을 때, 어떤 사람부터 순서대로 k번째 사람을 제외하며 계속해서 나가다가 마지막 남은 사람을 구하기!

import sys

N, K = [int(i) for i in sys.stdin.readline().split()]

# 연결리스트 세팅
ll = LinkedList(1)
#1부터 N까지 숫자를 가지는 연결리스트를 만들기위해 LinkedList 사용
#보통 1부터 시작해서 초기값 1로 셋팅
for i in range(2, N + 1):
    #이미 LinkedList에 1이 있기 때문에 2부터 시작하여 N번째 노드까지 추가하기 위해 (2, N+1) 사용
    ll.insert(i)
    
josephus = []
idx = K - 1

while ll.head.next is not None:
    #연결리스트가 빈 리스트가 될 때까지 반복문 실행
    idx %= N
    died_person = ll.delete(idx)
    josephus.append(died_person)
    idx += K - 1
    #인덱스는 -1이고
    N -= 1
    #사람은 줄고

josephus.append(ll.delete(0))

# result = '<'
# for i in josephus:
#     if i != josephus[-1]:
#         result += str(i) + ", "
#     else:
#         result += str(i) + ">"

result = '<'
for i in josephus:
    result += str(i) + ", "
    if i == josephus[-1]:
        result = result[:-2] + ">"
        #슬라이싱을 통해 마지막 두번째 문자까지의 부분을 선택
        
print(result)