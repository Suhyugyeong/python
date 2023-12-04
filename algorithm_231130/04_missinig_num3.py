#주어진 연속된 숫자에서 빠진 숫자를 찾기 - 반복문과 조건문 사용
#비효율적
class Solution:
    def missing_number(self, nums: list[int]) -> int:
        for i in range(len(nums) + 1): #len(nums) + 1은 리스트에 빠진 숫자가 있다면 그 숫자가 될 수 있도록 범위를 설정
            if i not in nums:
                #만약 i가 nums에 없으면 빠진 숫자니까 반환해라
                return i
            
sol = Solution()
nums = [9,6,4,2,3,5,7,0,1]
result = sol.missing_number(nums)
print(result)