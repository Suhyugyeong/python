class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        nums_dict = {}
        for i, v in enumerate(nums):
            gap = target - v
            if gap in nums_dict and i != nums_dict[gap]:
                return [i, nums_dict[gap]]
            nums_dict[v] = i

sol = Solution()
result = sol.two_sum([3, 2, 4], 6)
print(result)