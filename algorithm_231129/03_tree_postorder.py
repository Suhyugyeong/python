#후위순회
class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

# 후위순회는 좌측 -> 우측  -> 루트
def postorder(node):
    if node.left != ".":
        postorder(tree[node.left])
    if node.right != ".":
        postorder(tree[node.right])
    print(node.data, end=" ")
        
tree = {
    'A' : Node('A', 'B', 'C'),
    'B' : Node('B', 'D', 'E'),
    'C' : Node('C', 'F', 'G'),
    'D' : Node('D', 'H', '.'),
    'E' : Node('E', '.', '.'),
    'F' : Node('F', '.', '.'),
    'G' : Node('G', '.', '.'),
    'H' : Node('H', '.', '.')
}

postorder(tree['A'])
#H D E B F G C A 
#순회는 가장 하위 레벨의 노드에서 시작하여 점차 상위 레벨의 노드로 올라가는 과정이 아닙니다. 
#각 순회 방식에 따라 노드 방문 순서가 달라지며, 각각의 순회 방법은 트리의 구조를 다르게 표현합니다.