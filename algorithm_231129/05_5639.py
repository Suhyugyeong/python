#전위순회된 이진 트리를 받아 후위순회된 결과를 출력하는 함수

import sys
sys.setrecursionlimit(10**6)
#재귀 호출의 깊이 제한을 늘리는 부분


tree = [int(sys.stdin.readline()) for _ in range(9)]
#9개의 숫자를 입력받아 tree에 저장
#이때 입력받은 숫자는 전위순회된 이진 트리의 순서대로 저장되어 있음

def pre_to_post(tree):    
    def postorder(start, end):
        #현재 서브트리의 루트 노드를 기준으로 왼쪽 서브트리와 오른쪽 서브트리로 나누어 후위순회를 수행하는 재귀 함수
        if start > end:
            #일반적으로 시작 인덱스가 끝 인덱스보다 크면 해당 서브트리는 비어있다고 간주
            #왜냐, 서브트리에 노드가 하나도 없거나, 이미 방문한 노드로만 이루어졌다는 의미이기 때문
            #현재 서브트리가 비어있다, 즉 노드가 없는 경우 함수 종료
            #서브트리의 시작 인덱스 start는 현재 서브트리의 루트 노드를 가리키며, 
            #끝 인덱스 end는 현재 서브트리의 마지막 노드를 가리킵니다. 
            #즉, tree[start]는 현재 서브트리의 루트 노드의 값을, 
            #tree[end]는 현재 서브트리의 마지막 노드의 값을 나타냅니다.
            return
        div = end + 1 # 루트노드를 기준으로 왼쪽과 오른쪽으로 서브트리를 나누기 위해 사용
        # 루트노드보다 큰 값이 나오면, 해당 노드를 기준으로 왼쪽과 오른쪽으로 서브트리를 나눔!
        #초기값은 현재 서브트리의 끝 다음 인덱스로 설정
        for i in range(start + 1, end + 1):
            #현재 서브트리에서 루트 노드보다 큰 값을 찾아 div에 저장
            if tree[start] < tree[i]:
                div = i
                break
        postorder(start + 1, div - 1) # 왼쪽 서브트리 재귀 호출
        postorder(div, end) # 오른쪽 서브트리 재귀 호출
        print(tree[start]) # 중간 노드 출력
    postorder(0, len(tree) - 1) #후위순회 결과 출력
pre_to_post(tree)