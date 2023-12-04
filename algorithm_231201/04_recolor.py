#문자열 blocks에서 길이가 k인 부분문자열을 선택하여 'W'의 개수를 세고, 그 중에서 최소 'W' 개수를 반환하는 함수
class Solution:
    def minimum_recolors(self, blocks: str, k: int) -> int:
        #문자열 blocks와 정수 k를 입력받아 최소 W 개수를 반환
        min_count = len(blocks) #최소 W 개수를 저장할 변수 min_count를 초기화
        for i in range(len(blocks)-k+1):
            #부분문자열을 만들 때, 반복문이 마지막까지 진행될 수 있도록 하는 조건
            #부분문자열의 시작 인덱스를 나타내는 i가 문자열 blocks의 끝까지 갈 수 있도록 하는데 그 목적
            #예를 들어, 문자열의 길이가 10이고 k가 3일 때, 마지막 부분문자열의 시작 인덱스는 10 - 3 = 7이 됩니다.
            # 만약 반복문의 조건이 len(blocks)까지라면, 
            # 인덱스 7에서 시작하는 길이 3인 부분문자열을 만들지 못하게 되어 부분문자열이 완전하지 않게 됩니다.
            new_count = blocks[i:i+k].count('W')
            min_count = min(min_count, new_count)
        return min_count

sol = Solution()
print(sol.minimum_recolors('WBBWBBWBW', 7))

#뭔 말이여
# len(blocks): 문자열 'WBBWBBWBW'의 길이는 10입니다.
# len(blocks) - k + 1: 10 - 7 + 1 = 4입니다. 따라서 부분문자열을 만들 때 i의 범위는 0부터 3까지입니다.
# 각 부분문자열에서 'W'의 개수를 계산하여 최소값을 찾습니다.
# 부분문자열 'WBBWBBW'에서 'W'의 개수는 3개입니다.
# 부분문자열 'BBWBBWB'에서 'W'의 개수는 2개입니다.
# 부분문자열 'BWBBWBW'에서 'W'의 개수는 3개입니다.
# 부분문자열 'WBBWBWB'에서 'W'의 개수는 2개입니다.
# 따라서 최소 'W' 개수는 2입니다.