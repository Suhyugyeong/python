# 방법1. 리스트의 첫번째 요소와 마지막 요소의 합을 반환 *제일 좋은 방법
nums = input().split()
start, *_, end = nums
print(int(start) + int(end))

# 방법2. 리스트의 첫번째 요소와 마지막 요소의 합을 반환
nums = [int(i) for i in input().split()]
print(nums[0] + nums[-1])

# 방법3.리스트의 첫번째 요소와 마지막 요소의 합을 반환
nums = [int(i) for i in input().split()]
start_idx = 0
end_idx = len(nums) -1
print(nums[start_idx] + nums[end_idx])

# 방법4. 다 못 씀...
nums = [int(i) for i in input().split()]
