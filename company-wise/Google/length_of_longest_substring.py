# problem link : https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        L = [-1]*256
        max_len = 0
        n = len(s)
        while right < n:
            if L[ord(s[right])] != -1:
                left = max(L[ord(s[right])]+1,left)
            max_len = max(max_len, right-left+1)
            L[ord(s[right])] = right
            right += 1
        return max_len