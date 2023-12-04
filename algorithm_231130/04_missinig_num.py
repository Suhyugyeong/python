#0부터 n까지의 연속된 숫자 중 빠진 숫자를 찾는 함수

class Solution:
    def missing_number(self, nums: list[int]) -> int:
        # nums를 정렬한다.
        nums.sort()
        # nums = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        # nums의 길이만큼 0부터 반복한다. (i가 0, 1, 2, ...)
        for i, v in enumerate(nums):
            # 만약 i와 nums[i]가 다르면 -> 빠진 숫자는 i일 것이다.
            # enumerate를 통해 nums 리스트의 인덱스와 값을 튜플 형태로 반환
            if i != v:
                return i
        # 각 인덱스 i에 대해 nums[i]의 값이 i와 다르다면 빠진 숫자가 있는 것으로 간주하고 그 값을 반환
        return len(nums)

sol = Solution()
nums = [9,6,4,2,3,5,7,0,1]
result = sol.missing_number(nums)
print(result)