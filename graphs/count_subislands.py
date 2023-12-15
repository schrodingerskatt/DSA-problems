# Problem Link : https://leetcode.com/problems/count-sub-islands/

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:

        nr = len(grid2)
        nc = len(grid2[0])

        def dfs(r,c, flag):
            if r < 0 or c < 0 or r >= nr or c >= nc or grid2[r][c]==0:
                return 
            if grid1[r][c]!=grid2[r][c]:
                flag[0]=0
                return 
            grid2[r][c]=0
            dfs(r+1,c,flag)
            dfs(r,c+1,flag)
            dfs(r-1,c,flag)
            dfs(r,c-1,flag)
        
        subisland = 0
        for r in range(nr):
            for c in range(nc):
                if grid2[r][c]==1:
                    flag = [1]
                    dfs(r,c,flag)
                    if flag[0]:
                        subisland+=1
        return subisland