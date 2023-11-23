#https://leetcode.com/problems/valid-palindrome/

import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        srt = re.sub('[^a-z0-9]','',s.lower())
        return str == str[::-1]
#string은 불변이라 reverse가 안 됨
#대신 regex를 이용해서 변경 가능
    
    
    
import sys
s = sys.stdin.readline()
def reverse_list(lst):
    left, right = 0, len(lst) - 1
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
reverse_list(s)

