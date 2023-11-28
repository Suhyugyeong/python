#연결리스트를 기반으로 한 간단한 큐를 구현
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Queue:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head
        #queue는 head와 tail을 가지고 있으며 초기에 하나의 노드로 이루어져 있음
    def is_empty(self):
        return self.head is None
        #is_empty 메서드가 하는 일을 정의하는게 리턴값
        #현재 큐가 비어있으면 True를 반환하고, 비어있지 않으면 False를 반환
    def enqueue(self, data):
        #큐에 새로운 데이터 추가
        new_node = Node(data)
        self.tail.next = new_node
        self.tail = new_node
    def dequeue(self):
        #큐에서 제일 앞에 있는 데이터를 제거하고 반환
        if self.is_empty():
            return None
        data = self.head.data
        self.head = self.head.next
        return data
    def peek(self):
        #큐의 가장 앞에 있는 데이터를 조회
        if self.is_empty():
            return None
        return self.head.data