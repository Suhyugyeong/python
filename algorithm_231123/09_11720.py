import sys

sys.stdin.readline()
nums = sys.stdin.readline().rstrip()

result = 0
for i in nums:
    result += int(i)
print(result)