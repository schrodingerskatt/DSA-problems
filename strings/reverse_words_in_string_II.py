# Problem Link : https://leetcode.com/problems/reverse-words-in-a-string-ii/description/

class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
        i = 0
        for j in range(0, len(s)):
            if s[j]==" ":
                start = i
                end = j-1
                while start<=end and i < len(s) and j < len(s):
                    s[start],s[end]=s[end],s[start]
                    start+=1
                    end-=1
                i = j+1
            if j == len(s)-1:
                start = i
                end = j
                while start <= end:
                    s[start], s[end] = s[end],s[start]
                    start+=1
                    end-=1
        return s
                