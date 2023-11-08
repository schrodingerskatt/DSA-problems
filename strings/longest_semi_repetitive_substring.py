# Problem Link : https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/description/

class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        ans = 1
        pre = 0
        start = 0
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                if pre > 0:
                    start = pre
                pre = i
            ans = max(ans, i-start+1)
        return ans
