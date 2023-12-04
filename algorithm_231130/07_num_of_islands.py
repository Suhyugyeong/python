#2D 그리드에서 섬의 개수를 찾는 문제를 해결하기 위한 깊이 우선 탐색(DFS)을 사용한 해법
class Solution:
    def num_islands(self, grid: list[list[str]]) -> int:
        def dfs(i, j):
            # (상하좌우는 grid 범위 안에 있어야 하고, 1인 경우에는 찾아가서 0으로 변경)
            if i < 0 or i >= len(grid):
                return
            if j < 0 or j >= len(grid[0]):
                return
            if grid[i][j] != '1':
                return
            # 해당 위치를 0으로 변경
            grid[i][j] = '2'
            # 상하좌우를 체크
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)
            
        count = 0
        # 반복문 돌리기 for문이 두개!!! (grid[0][0] -> grid[3][4])
        for i in range(len(grid)):
            #2D 그리드를 순회하면서, 현재 위치의 값이 '1'인 경우 
            # dfs 함수를 호출하여 해당 위치를 포함하는 섬을 찾고, 찾은 섬의 개수를 count에 1 추가
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