class Solution:
    def fib(self, n: int) -> int:
        #fib 메서드를 클래스 내부에 정의
        temp_list = [0, 1]
        #리스트 생성해서 초기값으로 할당
        if n in temp_list:
            return n
        #피보나치 수열의 0번째와 1번째는 각각 0과 1이니께..
        for i in range(2, n + 1):
            temp_list.append(temp_list[i-1] + temp_list[i-2]) #이전 두 항을 더한 값을 새로운 항으로 추가
        return temp_list[-1]

sol = Solution()
print(sol.fib(6))

#피보나치 수열
#피보나치 수열의 첫 번째 항은 0이고, 두 번째 항은 1이다.

#규칙
# 세 번째 항부터는 이전 두 항의 합으로 정의됩니다. 
# 즉, n번째 항은 (n-1)번째 항과 (n-2)번째 항의 합으로 계산됩니다.
# 수학적으로 표현하면, F(n) = F(n-1) + F(n-2) (단, F(0) = 0, F(1) = 1).
