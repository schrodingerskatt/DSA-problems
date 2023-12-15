# Problem Link : https://leetcode.com/problems/surrounded-regions/description/

class Solution:
    def solve(self, board: List[List[str]]) -> None:

        nrow = len(board)
        ncol = len(board[0])

        def capture_O(r,c):
            if r < 0 or c < 0 or r >= nrow or c >= ncol or board[r][c]!="O":
                return 
            board[r][c]="C"
            capture_O(r+1,c)
            capture_O(r-1,c)
            capture_O(r,c+1)
            capture_O(r,c-1)

        
        for r in range(nrow):
            for c in range(ncol):
                if (board[r][c]=="O" and (r in [0, nrow-1] or c in [0, ncol-1])):
                    capture_O(r,c)

        for r in range(nrow):
            for c in range(ncol):
                if board[r][c]=="O":
                    board[r][c]="X"
        
        for r in range(nrow):
            for c in range(ncol):
                if board[r][c]=="C":
                    board[r][c]="O"