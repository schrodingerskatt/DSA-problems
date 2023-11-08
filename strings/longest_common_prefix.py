# Problem Link : https://leetcode.com/problems/longest-common-prefix/description/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        s1 = strs[0]
        s2 = strs[len(strs)-1]
        result = ""
        for i in range(0,len(s1)):
            if s1[i]==s2[i]:
                result+=s1[i]
            else:
                break
        return result
        