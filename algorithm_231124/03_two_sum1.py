class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                print(f"{i}번째 : {nums[i]} / {j}번째 : {nums[j]}")
                if nums[i] + nums[j] == target:
                    return [i, j]
                
sol = Solution()
result = sol.two_sum([2, 7, 11, 15], 9)
print(result)