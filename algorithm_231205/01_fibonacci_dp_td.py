#메모이제이션을 활용하여 피보나치 수열을 계산하는 class Solution, 재귀함수를 통해 계산
class Solution:
    def fib(self, n: int) -> int:
        def top_down(n: int, memo: list) -> int:
            #재귀적으로 피보나치 수열을 계산, 메모이제이션을 사용하여 중복 계산을 피함
            if n <= 1:
                return n
            elif memo[n] != 0:
                #메모이제이션을 체크하는 부분으로 memo[n]에 이미 계산된 값이 있다면, 즉 0이 아니라면 해당 값을 반환하고 함수 종료
                return memo[n]
            memo[n] = top_down(n - 1, memo) + top_down(n - 2, memo)
            #만약 memo[n]에 계산된 값이 없다면, 피보나치 수열 규칙에 따라 계산
            #재귀적으로 top_down 함수를 호출하며 메모이제이션을 사용하여 호출된 값을 memo[n]에 저장
            return memo[n]
            #재귀적으로 호출된 값이 계속해서 상위 호출 스택으로 전파되면서 최종적으로 n번째 피보나치수가 memo[n]에 저장
        memo = [0, 1] + [0] * (n -1)
        #메모이제이션을 위한 리스트 memo를 초기화
        #top_down함수에서 0번째와 1번째 항에 대한 값이 이미 알려져 있기 때문에 미리 초기화해서 재귀호출 사용
        #나머지부분은 0으로 초기화 (나머지 항에 대한 메모이제이션을 위한 공간 마련)
        return top_down(n, memo)

sol = Solution()
print(sol.fib(6))

# 메모이제이션(Memoization)은 컴퓨터 프로그램에서 동일한 계산이 반복되는 것을 방지하기 위해 
# 이전에 계산한 결과를 저장하고 재활용하는 최적화 기술입니다. 
# 이는 주로 재귀적인 알고리즘에서 중복 계산을 피하는데 활용되며, 
# 동적 계획법(Dynamic Programming)의 핵심 아이디어 중 하나입니다.

# 메모이제이션의 주요 아이디어는 한 번 계산한 값을 저장해 두고, 
# 나중에 같은 입력에 대한 계산이 필요할 때 저장된 값을 반환하는 것입니다. 
# 이를 통해 계산 복잡도를 줄이고 알고리즘의 성능을 향상시킬 수 있습니다.

# 피보나치 수열의 경우, 재귀적인 방법으로 계산하면 중복 계산이 많이 발생합니다. 
# 메모이제이션을 사용하면 중복 계산을 효과적으로 피할 수 있습니다. 
# 이를 위해 이미 계산된 값을 저장하는 자료구조, 일반적으로는 배열이나 딕셔너리 등을 사용합니다.

# 간단한 예로, 메모이제이션을 사용하지 않고 재귀적으로 피보나치 수열을 계산할 때는 
# 같은 값들을 여러 번 계산하게 되어 효율성이 떨어집니다. 
# 메모이제이션을 사용하면 한 번 계산한 값을 저장해 두어 다시 계산하지 않아도 되므로 효율적으로 계산할 수 있습니다.