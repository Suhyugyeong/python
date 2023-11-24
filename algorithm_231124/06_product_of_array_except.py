class Solution:
    def product_except_self(self, nums: list[int]) -> list[int]:
        # result = [1 for _ in nums]
        result = [1] * len(nums) # O(1)
        p = 1
        for i in range(len(nums) - 1):
            p *= nums[i]
            result[i+1] *= p
        
        p = 1
        for i in range(len(nums)-1, 0, -1):
            p *= nums[i]
            result[i-1] *= p
        
        return result
    
sol = Solution()
nums = [1, 2, 3, 4]
result = sol.product_except_self(nums)
print(result) # [24, 12, 8, 6]

#         / 1    / 1, 2 / 1, 2, 3
# 2, 3, 4 / 3, 4 / 4    /         