import sys

class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

def preorder(node):
    print(node.data, end = "")
    if node.left != ".":
        preorder(tree[node.left])
    if node.right != ".":
        preorder(tree[node.right])

def inorder(node):
    if node.left != ".":
        inorder(tree[node.left])
    print(node.data, end = "")
    if node.right != ".":
        inorder(tree[node.right])

def postorder(node):
    if node.left != ".":
        postorder(tree[node.left])
    if node.right != ".":
        postorder(tree[node.right])
    print(node.data, end = "")

N = int(sys.stdin.readline())
#트리의 노드수를 입력받기
tree = {}
#노드를 저장하기 위한 빈 딕셔너리 생성
#각 노드의 이름을 키로 하고, 해당 노드 객체를 값으로 가짐..
for i in range(N):
    #N번만큼 돌려서 각 노드에 대한 정보를 딕셔너리에 저장
    tree_list = sys.stdin.readline().split()
    #각 노드의 정보를 입력받기
    tree[tree_list[0]] = Node(tree_list[0], tree_list[1], tree_list[2])
    #data, left, right순

preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])