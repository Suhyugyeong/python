#역순으로 읽어도 같은말이나 구절 또는 숫자... 뛰어쓰기 구두점 조정은 허용
#다시합시다
#eye
#https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longest_palindrome(self, s: str) -> str:
        result = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                temp = s[i:j+1]
                if len(temp) > len(result):
                    if temp == temp[::-1]:
                        result = temp
        return result
                


sol = Solution()
result = sol.longest_palindrome("another level")
print(result) # level