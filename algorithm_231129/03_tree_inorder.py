#이진트리를 생성하고 중위순회 inordered traversal를 구현
class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

# 중위순회는 좌측 -> 루트 -> 우측
def inorder(node):
    if node.left != ".":
        #좌측 자식 노드가 점이 아닌 경우만 실행
        #즉, 좌측 자식이 존재하는 경우에만 좌측 자식으로 이동
        inorder(tree[node.left])
    print(node.data, end=" ")
    #이 구문이 실행될 때 출력되는 값은 현재 방문한 노드의 데이터(현재 노드 함수에서 불러온 tree[A])
    if node.right != ".":
        inorder(tree[node.right])
        
tree = {
    'A' : Node('A', 'B', 'C'),
    #key는 A : A라는 데이터를 가진 노드가 생성되며 이 노드 좌측 자식은 B, 우측 자식은 C 
    #tree는 딕셔너리 노드를 이용해 이진 트리를 나타내고 있음.. 비추.. 클래스를 사용해라..
    'B' : Node('B', 'D', 'E'),
    'C' : Node('C', 'F', 'G'),
    'D' : Node('D', 'H', '.'),
    'E' : Node('E', '.', '.'),
    #각각 자식을 가지지 않는 리프leaf 노드..
    'F' : Node('F', '.', '.'),
    'G' : Node('G', '.', '.'),
    'H' : Node('H', '.', '.')
}

inorder(tree['A'])
#H D B E A F C G 