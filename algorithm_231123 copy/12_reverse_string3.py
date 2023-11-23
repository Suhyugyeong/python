class Solution:
    def reverse_string(self, s: list[str]) -> None:
        s[:] = s[::-1]

sol = Solution()
s = ["h","e","l","l","o"]
sol.reverse_string(s)

print(s) # ["o","l","l","e","h"]