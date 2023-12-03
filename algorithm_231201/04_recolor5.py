class Solution:
    def minimum_recolors(self, blocks: str, k: int) -> int:
        i = 0
        result = []
        while i <= len(blocks) - k:
            s = blocks[i:i + k]
            if len(s) == k:
                result.append(s.count('W'))
            i += 1
        return min(result)

sol = Solution()
print(sol.minimum_recolors('BWWWBB', 6))