
class Solution:
    def minimum_recolors(self, blocks: str, k: int) -> int:
        window = blocks[:k]
        min_count = window.count('W')
        
        # k번 인덱스부터 끝까지 돌려서 윈도우를 다시 만든다. 
        for i in range(k, len(blocks)):
            window = window[1:] + blocks[i] 
            # 윈도우의 길이를 유지하면서 앞의 글자 하나를 빼고, 다음 인덱스의 글자를 추가하여 새로운 윈도우를 생성
            new_count = window.count('W')
            # 해당 윈도우의 카운트를 구함 
            min_count = min(min_count, new_count)
            # 최소카운트와 해당 카운트의 최소 카운트 구함 
        return min_count

sol = Solution()
print(sol.minimum_recolors('WBBWBBWBW', 7))