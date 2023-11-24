class Solution:
    def three_sum(self, nums: list[int]) -> list[list[int]]:
        result = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        temp = [nums[i], nums[j], nums[k]]
                        temp.sort()
                        if temp not in result:
                            result.append(temp)
        return result

sol = Solution()
nums = [-1,0,1,2,-1,-4]
result = sol.three_sum(nums)
print(result) # Output: [[-1,-1,2],[-1,0,1]]