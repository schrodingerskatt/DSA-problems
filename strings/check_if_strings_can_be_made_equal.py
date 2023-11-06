# problem link : https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-i/description/

class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        s1 = list(s1)
        for i in range(0,len(s1)-2):
            s1[i],s1[i+2] = s1[i+2],s1[i]
            if s1[i]==s2[i] and s1[i+2]==s2[i+2]:
                continue
            else:
                s1[i],s1[i+2] = s1[i+2],s1[i]
        s1 = ''.join(s1)
        return s1==s2
