class Solution:
    def minimum_recolors(self, blocks: str, k: int) -> int:
        window = blocks[:k]
        min_count = window.count('W')
        
        # k번 인덱스부터 끝까지 돌려서 윈도우를 다시 만든다. 
        for i in range(k, len(blocks)):
            # 앞의 글자 하나 빼고, 그 다음 인덱스를 붙여 윈도우를 생성 
            window = window[1:] + blocks[i] 
            # 해당 윈도우의 카운트를 구함 
            new_count = window.count('W')
            # 최소카운트와 해당 카운트의 최소 카운트 구함 
            min_count = min(min_count, new_count)
        return min_count

sol = Solution()
print(sol.minimum_recolors('WBBWBBWBW', 7))