class Solution:
    def missing_number(self, nums: list[int]) -> int:
        n = len(nums)
        total = (n * (n + 1)) // 2
        result = total - sum(nums)
        return result

sol = Solution()
nums = [9,6,4,2,3,5,7,0,1]
result = sol.missing_number(nums)
print(result)