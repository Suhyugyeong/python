# WORST
class Solution:
    def missing_number(self, nums: list[int]) -> int:
        for i in range(len(nums) + 1):
            if i not in nums:
                return i
            
sol = Solution()
nums = [9,6,4,2,3,5,7,0,1]
result = sol.missing_number(nums)
print(result)