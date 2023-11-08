# Problem Link : https://leetcode.com/problems/zigzag-conversion/description/

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        ans=""
        increment = 2*(numRows-1)
        for i in range(0,numRows):
            for j in range(i,len(s),increment):
                 ans+=s[j]
                 if (i > 0 and i < numRows-1 and j+increment-2*i < len(s)):
                     ans+=s[j+increment-2*i]
        return ans

