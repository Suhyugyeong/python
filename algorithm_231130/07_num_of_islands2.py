class Solution:
    def num_islands(self, grid: list[list[str]]) -> int:
        def dfs(i, j):
            # 해당 위치를 0으로 변경
            grid[i][j] = '2'
            # 상하좌우를 체크
            direction = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
            # (상하좌우는 grid 범위 안에 있어야 하고, 1인 경우에는 찾아가서 0으로 변경)
            for d_i, d_j in direction:
                if d_i < 0 or d_i >= len(grid):
                    continue
                if d_j < 0 or d_j >= len(grid[0]):
                    continue
                if grid[d_i][d_j] != '1':
                    continue
                dfs(d_i, d_j)
        count = 0
        
        # 반복문 돌리기 for문이 두개!!! (grid[0][0] -> grid[3][4])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # grid[i][j]이 1인 경우 ->
                if grid[i][j] == '1':
                    dfs(i, j)
                    # 체크까지 끝났다! 그 때 섬의 개수 + 1
                    count += 1
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