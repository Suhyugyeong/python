class Solution:
    def minimum_recolors(self, blocks: str, k: int) -> int:
        i = 0
        result = []
        # 각 부분문자열에서 'W'의 개수를 저장할 리스트 result를 초기화
        while i <= len(blocks) - k:
            s = blocks[i:i + k]
            if len(s) == k:
                result.append(s.count('W'))
            i += 1 #이부분이 애매하네..
        return min(result)

sol = Solution()
print(sol.minimum_recolors('BWWWBB', 6))