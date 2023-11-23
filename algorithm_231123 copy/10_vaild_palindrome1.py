class Solution:
    def isPalindrome(self, s: str) -> bool:
        str_list = [char.lower() for char in s if char.isalnum()]
        while len(str_list) > 1:
            if str_list.pop(0) != str_list.pop():
                return False
        return True
    
sol = Solution()
print(sol.isPalindrome(""))