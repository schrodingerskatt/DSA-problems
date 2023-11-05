# problem link : https://leetcode.com/problems/merge-strings-alternately/description/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = 0
        if len(word1)<len(word2):
            l = len(word1)
        else:
            l = len(word2)
        ans = ""
        k = 0
        for i in range(0,l):
            k = i
            ans = ans + word1[i]+word2[i]
        if l < len(word1):
            for i in range(k+1,len(word1)):
                ans = ans+word1[i]
        if l < len(word2):
            for i in range(k+1,len(word2)):
                ans = ans+word2[i]
        return ans

        