import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        str = re.sub('[^a-z0-9]', '', s.lower())
        return str == str[::-1]
    
sol = Solution()
print(sol.isPalindrome("race a car"))