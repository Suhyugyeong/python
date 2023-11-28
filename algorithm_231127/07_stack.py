#스택 자료구조를 클래스로 구현한 것
#노드클래스와 스택클래스가 정의되어 있음
class Node:
    #Node 클래스는 연결 리스트의 노드를 나타냄..
    def __init__(self, data):
        self.data = data
        self.next = None
        #각 노드는 데이터와 다음 노드를 가리키는 링크next로 이루어짐..
class Stack:
    def __init__(self):
        self.head = None
        #클래스는 스택의 맨 위 노드를 head로 가리키는 형태로 구현
    def is_empty(self):
        return self.head is None
        # if self.head is None:
        #     return True
        # else:
        #     return False
    def push(self, data):
        #스택에 원소를 추가하는 메서드
        new_node = Node(data)
        #추가할 노드는 data를 가지며 next는 현재로서는 None
        new_node.next = self.head
        #추가할 노드 다음 노드를 현재 스택의 맨 위 노드(self.head)로 설정함으로 새로운 노드가 기존의 맨 위 노드를 가리킴
        self.head = new_node
        #스택의 맨 위 노드를 새 노드로 업데이트
    def pop(self):
        if self.is_empty():
            return None
        data = self.head.data
        #제거할 노드의 데이터를 data 변수에 저장
        self.head = self.head.next
        #스택 맨 위의 노드를 다음 노드로 업데이트하여, 맨 위 노드를 제거(맨 위의 원소 제거)
        return data
    def peek(self):
        if self.is_empty():
            return None
        return self.head.data

stack = Stack()
stack.push('a')
stack.push('b')
stack.push('c')
print(stack.head.data) #c
print(stack.head.next.data) #b
print(stack.head.next.next.data) #a
#stack.head.data는 스택의 맨 위에 있는 노드의 데이터를 나타내고, 
#stack.head.next.data는 그 아래에 있는 노드의 데이터를 나타내게 됩니다.