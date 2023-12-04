class Solution:
    def minimum_recolors(self, blocks: str, k: int) -> int:
        middle_str = blocks[:k] # WBBWBBW
        result = middle_str.count('W')

        for i in range(k, len(blocks)):
            middle_str = middle_str[1:] + blocks[i]
            if middle_str.count("W") == 0:
                result = 0
            elif blocks[i] == "W":
                pass
            # middle_str 자체에 이미 'W'의 개수가 반영되어 있고, 
            #새로운 글자가 'W'일 경우에는 추가적인 작업이 필요하지 않음
            elif middle_str.count("W") < result:
                result = middle_str.count("W")
                #새로운 윈도우에서 'W'의 개수가 현재까지의 최소 'W' 개수보다 작으면, result를 해당 개수로 업데이트
        return result

sol = Solution()
print(sol.minimum_recolors('WBBWBBWBW', 7))