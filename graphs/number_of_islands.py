# Problem Link : https://leetcode.com/problems/number-of-islands/description/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        nr = len(grid)
        nc = len(grid[0])

        def dfs(r,c):
            nonlocal nr, nc
            grid[r][c]=0

            if r-1>=0 and grid[r-1][c]=="1":
                dfs(r-1,c)
            if r+1< nr and grid[r+1][c]=="1":
                dfs(r+1,c)
            if c-1>=0 and grid[r][c-1]=="1":
                dfs(r,c-1)
            if c+1<nc and grid[r][c+1]=="1":
                dfs(r,c+1)

        if not grid:
            return 0
        nr = len(grid)
        nc = len(grid[0])
        islands = 0
        for i in range(nr):
            for j in range(nc):
                if grid[i][j]=="1":
                    dfs(i,j)
                    islands+=1
        return islands
        
        