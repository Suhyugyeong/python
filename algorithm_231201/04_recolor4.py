from collections import deque

class Solution:
    def minimum_recolors(self, blocks: str, k: int) -> int:
        paint = deque(blocks[:k])
        now_paint = paint
        min_count = now_paint.count("W")
        
        for i in range(int(len(blocks)) - k) :
            now_paint.popleft()
            now_paint.append(blocks[k+i]) 
            count = now_paint.count("W")
            min_count = min(min_count, count)
        
        return min_count

sol = Solution()
print(sol.minimum_recolors('WBBWBBWBW', 7))