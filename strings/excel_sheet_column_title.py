# Problem Link : https://leetcode.com/problems/excel-sheet-column-title/

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:

        ans = ""
        while columnNumber > 0:
            columnNumber -= 1
            ans = ans + chr((columnNumber) % 26 + ord('A'))
            columnNumber = (columnNumber)//26
        ans = ans[::-1]
        return ans
        