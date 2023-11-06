# Problem Link : https://leetcode.com/problems/faulty-keyboard/description/

class Solution:
    def finalString(self, s: str) -> str:
        count_i  = 0
        ans = ""
        for i in range(0,len(s)):
            if s[i] == 'i':
                ans = ans[::-1]
            else:
                ans+=s[i]
        return ans

        