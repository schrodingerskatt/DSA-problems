# Problem Link : https://leetcode.com/problems/sudoku-solver/description/

from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    for num in "123456789":
                        if self.isvalid(i, j, num, board):
                            board[i][j] = num
                            if self.solveSudoku(board):
                                return True
                            else:
                                board[i][j] = '.'
                    return False
        return True

    def isvalid(self, row, col, val, board):
        for i in range(9):
            if board[row][i] == val:
                return False
            if board[i][col] == val:
                return False
            if board[3 * (row // 3) + (i // 3)][3 * (col // 3) + (i % 3)] == val:
                return False
        return True
