# Problem Link : https://leetcode.com/problems/lexicographically-smallest-string-after-substring-operation/description/

class Solution:
    def smallestString(self, s: str) -> str:
        s = list(s)
        pos = -1
        for i, char in enumerate(s):
            if char != 'a':
                pos = i
                break

        if pos == -1:
            return "".join(s[:-1]) + 'z'
        else:
            for i in range(pos,len(s)):
                if s[i]!='a':
                    s[i] = chr(ord(s[i])-1)
                else:
                    break
        return "".join(s)