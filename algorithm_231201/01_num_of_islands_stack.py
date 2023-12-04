#섬의 개수 세기
#2차원 그리드에서 1로 표시된 영역이 섬, 주어진 그리드에서 섬의 개수 찾기

class Solution:
    def num_islands(self, grid: list[list[str]]) -> int:
        count = 0 #섬 개수 초기화
        # 반복문 돌리기 for문이 두개!!! (grid[0][0] -> grid[3][4])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # grid[i][j]이 1인 경우 ->
                if grid[i][j] == '1':
                    count += 1
                    stack = [(i, j)] #해당 셀의 좌표를 stack에 추가하기
                    while stack:
                        (y, x) = stack.pop()
                        direction = [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)]
                        for new_y, new_x in direction:
                            if 0 <= new_y < len(grid) and 0 <= new_x < len(grid[0]) and grid[new_y][new_x] == "1":
                                grid[new_y][new_x] = "0" #해당 지점 이미 방문
                                stack.append((new_y, new_x))
        return count

sol = Solution()
grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]
result = sol.num_islands(grid)
print(result)