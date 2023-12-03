#candidates에서 합이 특정 값 target이 되는 모든 조합을 찾는 함수인 combination_sum을 구현
#코드 구조는 재귀적 깊이 우선 탐색(DFS)을 사용
#한놈만 패기

def combination_sum(candidates, target):
    results = []
    #최종 결과를 저장할 리스트
    result = []
    #현재까지의 조합을 저장할 리스트
# 재귀 호출이 깊어짐에 따라 result 리스트에는 다양한 조합이 임시로 담기게 됩니다. 
# 그러나 이 조합들 중에서 목표값에 도달하는 유효한 조합을 찾으면 그때마다 results 리스트에 복사본을 추가합니다.
# 만약 result와 results를 나누지 않는다면, 재귀 호출의 각 단계에서 result를 조작할 때 동시에 results에도 영향을 미치게 되어 올바른 결과를 얻기 어려워집니다. 
# 따라서 각각의 재귀 호출에서 result와 results를 따로 사용함으로써 각각의 조합을 정확하게 추적할 수 있습니다.
    def dfs(idx, target):
        if target < 0:
            #여기서 target은 현재까지의 후보를 더했을 때 합계인데 이게 음수면 더 이상 진행할 필요가 없음.
            return
        elif target == 0: 
# 재귀 호출을 통해 숫자를 선택하고 target 값을 갱신합니다. 선택된 숫자의 값을 현재 target에서 빼면서 재귀 호출을 진행합니다.

# 예를 들어, candidates = [2, 3, 6, 7], target = 7의 경우:
# 처음에는 target은 7입니다.
# 첫 번째 단계에서 2를 선택합니다. 그러면 target은 7 - 2 = 5가 됩니다.
# 두 번째 단계에서 3을 선택합니다. 그러면 target은 5 - 3 = 2가 됩니다.
# 세 번째 단계에서 2를 선택합니다. 그러면 target은 2 - 2 = 0이 됩니다.
# 이때 target이 0이 되었으므로, 이때까지 선택한 숫자들 [2, 3, 2]이 목표값 7을 만족하는 조합입니다. 
            results.append(result[:])
            #현재까지의 숫자들로 이루어진result의 복사본을 results 리스트에 추가
            #이를 통해 results 리스트에 모든 유효한 조합이 별도의 리스트로 기록 ([:] 리스트의 모든요소를 얕은 복사)
            return
        #후보 순회하며 조합 찾기
        for i in range(idx, len(candidates)): #i를 활용해 중복을 허용
            result.append(candidates[i]) #현재 후보 현재까지 조합에 추가
            new_target = target - candidates[i] #타겟에서 현재 후보 값을 뺌
            dfs(i, new_target) #재귀호출
            result.pop() #현재 추가한 후보를 다시 제거하여 다른 조합 탐색 : 백트래킹
    dfs(0, target)
    return results

candidates = [2, 3, 6, 7]
target = 7
#candidates에서 합이 7이 되는 모든 조합 찾기!
print(combination_sum(candidates, target))

# [2, 3, 6, 7]을 반복!
# 1. [2]
# target = target - 2
    # [2, 3, 6, 7]을 반복!
    # 1. [2]
    # target = target - 2 !!! 만약 target이 0이면 결과에 저장! (만약 0보다 작으면 중단)
        # [2, 3, 6, 7]을 반복!
        
    # 2. [3]
    # target = target - 3
        # [3, 6, 7]을 반복!
        
    # 3. [6]
    # target = target - 6
        # [6, 7]을 반복!
    # 4. [7]
    # target = target - 7

# 2. [3]
# target = target - 3
    # [3, 6, 7]을 반복!

# 3. [6]
# target = target - 6
    # [6, 7]을 반복!

# 4. [7]
# target = target - 7