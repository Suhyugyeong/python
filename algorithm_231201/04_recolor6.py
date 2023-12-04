class Solution:
    def minimum_recolors(self, blocks: str, k: int) -> int:
        ans = cnt = blocks[:k].count('W')
        
        for i in range(k, len(blocks)):
            cnt += blocks[i] == 'W'
            #새로운 글자가 'W'인 경우, 'W'의 개수를 증가
            cnt -= blocks[i -k] == 'W'
            #이전 부분문자열에서 빠진 글자가 'W'인 경우, 'W'의 개수를 감소
            ans = min(ans, cnt)
            #cnt는 현재까지의 부분문자열에서 W의 개수를 유지하면서 이동
            #ans에는 최소값이 계속 업데이트
        return ans

sol = Solution()
print(sol.minimum_recolors('WBBWBBWBW', 7))

#굳이 ans가 최소값일텐데 cnt랑 min 함수를 쓰는게 이해가 안 돼서.. gpt는 아래도 괜찮대..
# class Solution:
#     def minimum_recolors(self, blocks: str, k: int) -> int:
#         ans = cnt = blocks[:k].count('W')
        
#         for i in range(k, len(blocks)):
#             cnt += blocks[i] == 'W'
#             cnt -= blocks[i - k] == 'W'
#             ans = cnt  # 직접 ans에 cnt 값을 할당
#         return ans
