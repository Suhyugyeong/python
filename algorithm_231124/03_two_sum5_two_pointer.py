# 투포인터라고 해서, 반드시 정렬이 필요한 것은 아님!
# 하지만 대부분 투포인터는 정렬이 필요하다.
# 
# 이 문제는 정렬이 필요한 보편적인 문제! 하지만 인덱스 값이 변경되면 안되기 때문에 제출은 불가능!
# 그냥, 투 포인터 기법에 대해 이해하기 위해 풀어봤다!

class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        lt = 0
        rt = len(nums)-1
        
        while lt < rt:
            temp_sum = nums[lt] + nums[rt]
            if target == temp_sum:
                return [lt, rt]
            elif  target < temp_sum:
                rt -= 1
            elif  target > temp_sum:
                lt += 1
                
sol = Solution()
result = sol.two_sum([2, 7, 11, 15], 9)
print(result)