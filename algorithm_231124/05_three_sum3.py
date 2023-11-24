# 브루트포스 방법이 아닌, 투 포인터 기법을 활용해 문제를 풀이해야 시간초과에서 벗어날 수 있습니다.
# 시간복잡도 O(n^3) -> 시간복잡도 O(n^2)

class Solution:
    def three_sum(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort()        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            lt = i + 1
            rt = len(nums) - 1
            while lt < rt:
                temp_sum = nums[i] + nums[lt] + nums[rt]
                if 0 == temp_sum:
                    result.append([nums[i], nums[lt], nums[rt]])
                    while lt < rt and nums[lt] == nums[lt+1]:
                        lt += 1
                    while lt < rt and nums[rt] == nums[rt-1]:
                        rt -= 1
                    lt += 1
                    rt -= 1
                elif 0 < temp_sum:
                    rt -= 1
                elif 0 > temp_sum:
                    lt += 1
        return result
    
sol = Solution()
nums = [-1,0,1,2,-1,-4]
result = sol.three_sum(nums)
print(result) # Output: [[-1,-1,2],[-1,0,1]]