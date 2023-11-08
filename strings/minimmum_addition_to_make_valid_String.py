# Problem Link : https://leetcode.com/problems/minimum-additions-to-make-valid-string/description/

class Solution:
    def addMinimum(self, word: str) -> int:
        letters = ['a','b','c']
        i = 0
        ans = 0
        while i < len(word):
            for c in letters:
                if i < len(word) and c == word[i]:
                    i+=1
                else:
                    ans+=1
            return ans
                
                   
        
           