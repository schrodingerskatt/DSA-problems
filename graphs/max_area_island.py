# Problem Link : https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        max_area = 0
        visited = [[False for c in range(m)]for r in range(n)]

        def dfs(i,j):
      
            if i < 0 or i >= n or j < 0 or j >= m or grid[i][j]==0 or visited[i][j]==True:
                return 0
            visited[i][j]=True
            count=1
            count+=dfs(i+1,j)
            count+=dfs(i,j+1)
            count+=dfs(i-1,j)
            count+=dfs(i,j-1)
            return count
    


        for r in range(n):
            for c in range(m):
                if grid[r][c]==1 and visited[r][c]==False:
                    area = dfs(r,c)
                    max_area = max(max_area,area)
        return max_area
        