class Solution:
    def reverse_string(self, s: list[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        

sol = Solution()
s = ["h","e","l","l","o"]
sol.reverse_string(s)

print(s) # ["o","l","l","e","h"]