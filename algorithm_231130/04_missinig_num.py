class Solution:
    def missing_number(self, nums: list[int]) -> int:
        # nums를 정렬한다.
        nums.sort()
        # nuns = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        # nums의 길이만큼 0부터 반복한다. (i가 0, 1, 2, ...)
        for i, v in enumerate(nums):
            # 만약 i와 nums[i]가 다르면 -> 빠진 숫자는 i일 것이다.
            if i != v:
                return i
        # 반복문이 다 돌았다면 맨 마지막이 빠진 것이다.
        return len(nums)

sol = Solution()
nums = [9,6,4,2,3,5,7,0,1]
result = sol.missing_number(nums)
print(result)