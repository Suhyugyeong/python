#주어진 자연수 N과 M에 대해 1부터 N까지의 숫자 중에서 중복없이 길이가 M인 수열을 찾아내는 깊이 우선 탐색(DFS) 알고리즘
import sys
N, M = [int(i) for i in sys.stdin.readline().split()]
nums = [i for i in range(1, N + 1)] #1부터 N까지의 숫자를 리스트로 생성

def dfs(path): #dfs 함수는 현재까지 선택된 수열을 나타내는 path를 매개변수로 받는다
    #path는 현재까지 선택된 숫자들을 담은 리스트
    if len(path) == M:
        print(*path)
        return
    for i in nums:
        if i not in path: #선택된 숫자가 현재까지의 수열에 포함되지 않았다면, 해당 숫자를 path에 추가
            path.append(i)
            dfs(path) #재귀적으로 다음 숫자를 선택하러 이동
            path.pop() #이전 상태로 되돌아감 (백트래킹) : 중복없이 길이가 M인 수열을 찾기 위해 사용
            
dfs([]) #초기 경로가 빈 리스트인 상태로 DFS를 시작
