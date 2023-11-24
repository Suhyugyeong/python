class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        for i, v in enumerate(nums):
            gap = target - v
            extra_nums = nums[i+1:]
            if gap in extra_nums:
                return [i, extra_nums.index(gap) + i + 1]
                
sol = Solution()
result = sol.two_sum([2, 7, 11, 15], 18)
print(result)