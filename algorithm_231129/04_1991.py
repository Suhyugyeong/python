import sys

def preorder(node):
    print(node, end="")
    #현재 노드 값 출력
    #루트 출력
    if tree[node][0] != ".":
        #"."은 트리에 자식이 없음을 나타내는 관용적 표현
        preorder(tree[node][0])
        #현재 노드의 왼쪽 자식 
        #node라는 현재 노드에 대한 정보가 담긴 리스트에서 첫번째 원소를 나타내고, 그게 해당 노드의 왼쪽 자식 노드의 이름을 의미
    if tree[node][1] != ".":
        preorder(tree[node][1])
        #현재 노드의 오른쪽 자식

def inorder(node):
    if tree[node][0] != ".":
        inorder(tree[node][0])
    print(node, end="")
    if tree[node][1] != ".":
        inorder(tree[node][1])

def postorder(node):
    if tree[node][0] != ".":
        postorder(tree[node][0])
    if tree[node][1] != ".":
        postorder(tree[node][1])
    print(node, end="")
    
N = int(sys.stdin.readline())
tree = {}
for _ in range(N):
    data, left, right = sys.stdin.readline().split() # A B C / B D .
    tree[data] = (left, right)
# tree = {'A': ('B', 'C'), 'B': ('D', '.'), 'C': ('E', 'F'), 'E': ('.', '.'), 'F': ('.', 'G'), 'D': ('.', '.'), 'G': ('.', '.')}

preorder('A')
print()
inorder('A')
print()
postorder('A')