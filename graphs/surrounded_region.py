# Problem Link : https://leetcode.com/problems/surrounded-regions/description/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n = len(board)
        m = len(board[0])

        def dfs(i,j):
            if i < 0 or j < 0 or i >=n or j >=m or board[i][j]!='O':
                return 
            board[i][j]='C'
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)

        for r in range(n):
            for c in range(m):
                if board[r][c]=='O' and (r in [0,n-1] or c in [0,m-1]):
                    dfs(r,c)
        for r in range(n):
            for c in range(m):
                if board[r][c]=='O':
                    board[r][c]='X'
        
        for r in range(n):
            for c in range(m):
                if board[r][c]=='C':
                    board[r][c]='O'

'''
1. This problem is a prime example of what reverse thinking is, always remember if you can't solve a
   graph or matrix problem straight away, try reverse thinking.
2. Let's say there is a rectangle divided into 2 parts 'A' and 'B', saying I want only 'A' part is same
   as I don't want anythong except 'B'.
3. Hence, the problem breakdowns to (capturing surrounded region) => (capture everything except unsurrounded region).

4. So, we have to look only those surrounded zeros that are not on border.
5. We would go for border 0's apply dfs on it and change them to some character let's say 'C'.
6. Now, we will be left with captured O's on our board, change them to 'X'.
7. Now, convert all the captured 'C''s to 'X's.

'''