# Problem Link : https://leetcode.com/problems/excel-sheet-column-number/description/

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:

        i = len(columnTitle)-1
        value = 0
        j = 0
        while i >=0:
            value = value + ((ord(columnTitle[i])-65)+1)*pow(26,j)
            j+=1
            i-=1
        return value
        