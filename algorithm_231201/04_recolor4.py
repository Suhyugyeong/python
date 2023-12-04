from collections import deque #덱(deque)?

class Solution:
    def minimum_recolors(self, blocks: str, k: int) -> int:
        paint = deque(blocks[:k])
        now_paint = paint
        min_count = now_paint.count("W")
        
        for i in range(int(len(blocks)) - k) :
            #전체 문자열의 길이에서 부분문자열의 길이 k를 뺀 값은, 
            #부분문자열을 생성할 수 있는 시작 인덱스의 범위를 나타냄 
            #이 범위에서 시작하는 모든 부분문자열을 생성하고 탐색하려고 함..
            now_paint.popleft()
            now_paint.append(blocks[k+i]) 
            #가장 왼쪽 원소를 제거, 부분문자열의 길이를 유지하며 가장 오른쪽에 현재 인덱스의 글자를 추가
            count = now_paint.count("W")
            min_count = min(min_count, count)
        
        return min_count

sol = Solution()
print(sol.minimum_recolors('WBBWBBWBW', 7))