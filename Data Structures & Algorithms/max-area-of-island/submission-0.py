class Solution:
    def maxAreaOfIsland(self, grid: List[List[str]]) -> int:
        max_area = 0
        def dfs(i,j):
            area = 0
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                return 0
            if grid[i][j] == 0:
                return 0
            else:
                area += 1

            grid[i][j] = 0
            area += dfs(i-1,j)
            area += dfs(i + 1,j)
            area += dfs(i,j - 1)
            area += dfs(i,j + 1)

            return area
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area = dfs(i,j)
                    max_area = max(area,max_area)

        return max_area