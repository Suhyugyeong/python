#주어진 연속된 숫자에서 빠진 숫자를 찾는 방법으로 수학적 접근을 사용
class Solution:
    def missing_number(self, nums: list[int]) -> int:
        n = len(nums)
        total = (n * (n + 1)) // 2 
        #등차수열의 합을 이용하여 0부터 n까지 전체 합을 계산
        result = total - sum(nums)
        #주어진 리스트 nums의 합을 구하고, 전체 합에서 빼서 빠진 숫자 찾기
        return result

sol = Solution()
nums = [9,6,4,2,3,5,7,0,1]
result = sol.missing_number(nums)
print(result) #8