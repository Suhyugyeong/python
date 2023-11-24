#https://leetcode.com/problems/group-anagrams/description/
import collections


class Solution:
    def group_anagrams(self, strs: list[str]) -> list[list[str]]:
        # 일반 딕셔너리에서는 '없는 키'를 조회했을 때, 에러(Key Error)가 난다!
        anagrams = collections.defaultdict(list)
        for i in strs:
            anagrams[''.join(sorted(i))].append(i)
        return list(anagrams.values())

sol = Solution()
result = sol.group_anagrams(["eat","tea","tan","ate","nat","bat"])
print(result)