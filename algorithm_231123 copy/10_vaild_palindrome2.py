from collections import deque

class Solution:
    def isPalindrome(self, s: str) -> bool:
        str_list = deque([char.lower() for char in s if char.isalnum()])
        while len(str_list) > 1:
            if str_list.popleft() != str_list.pop():
                return False
        return True
    
sol = Solution()
print(sol.isPalindrome(""))