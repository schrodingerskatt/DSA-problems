# Problem Link : https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        nrow = len(grid)
        ncol = len(grid[0])
        fresh=0
        for r in range(nrow):
            for c in range(ncol):
                if grid[r][c]==1:
                    fresh+=1
                if grid[r][c]==2:
                    q.append([r,c])
        time = 0
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        while q and fresh > 0:
            for i in range(len(q)):
                r,c = q.pop()
                for dr, dc in directions:
                    row, col = r+dr, c+dc
                    if row < 0 or col < 0 or row >= nrow or col >= ncol or grid[row][col]!=1:
                        continue
                    grid[row][col]=2
                    q.append([row,col])
                    fresh-=1
            time+=1
        return time if fresh == 0 else -1
