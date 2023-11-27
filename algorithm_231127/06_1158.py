class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
    
    def insert(self, value):
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = Node(value)
    
    def get_node(self, index):
        current = self.head
        count = 0
        while count < index:
            count += 1
            current = current.next
        return current
    
    def delete(self, index):
        if index == 0:
            del_node = self.head.data
            self.head = self.head.next
            return del_node
        node = self.get_node(index - 1)
        del_node = node.next.data
        node.next = node.next.next
        return del_node


import sys

N, K = [int(i) for i in sys.stdin.readline().split()]

# 연결리스트 세팅! (1 ~ N까지 숫자 삽입)
ll = LinkedList(1)
for i in range(2, N + 1):
    ll.insert(i)
    
josephus = []
idx = K - 1

while ll.head.next is not None:
    idx %= N
    died_person = ll.delete(idx)
    josephus.append(died_person)
    idx += K - 1
    N -= 1

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
        
print(result)