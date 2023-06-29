class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        n = len(grid)
        m = len(grid[0])
        seen = [[False for i in range(m)] for j in range(n)]

        def dfs(i, j):
            if (i not in range(0, n)) or (j not in range(0, m)) or grid[i][j] == "0" or seen[i][j] == True:
                return
            if grid[i][j] == "1":
                seen[i][j] = True
                dfs(i, j+1)
                dfs(i, j-1)
                dfs(i+1, j)
                dfs(i-1, j)

        islands = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and seen[i][j] == False:
                    islands += 1
                    dfs(i, j)

        return islands



