class Solution:
    def longest_palindrome(self, s: str) -> str:
        def check(lt: int, rt: int):
            while lt >= 0 and rt <= len(s) - 1 and s[lt] == s[rt]:
                lt -= 1
                rt += 1
            return s[lt+1:rt]
        result = ''
        if len(s) < 2 or s == s[::-1]:
            result = s
        else:
            for i in range(len(s) - 1):
                print(result, check(i, i+2), check(i, i+1))
                result = max(result, check(i, i+2), check(i, i+1), key=len)
        return result
    
sol = Solution()
result = sol.longest_palindrome("babad")
print(result) # level