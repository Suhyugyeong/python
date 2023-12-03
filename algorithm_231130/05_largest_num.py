class Solution:
    def largest_number(self, nums: list[int]) -> str:
        nums = [str(i) for i in nums]        
        nums.sort(key=lambda x:(x*9), reverse=True)
        # nums = ''.join(nums)
        # if nums[0] == '0':
        #     return '0'
        # else:
        #     return nums
        return str(int(''.join(nums)))
    
sol = Solution()
nums = [3,30,34,5,9]
result = sol.largest_number(nums)
print(result)