# Problem Link : https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/description/

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        freq = {}
        l , ans = 0, 0
        for r in range(0,len(s)):
            freq[s[r]] = 1+freq.get(s[r],0)
            while len(freq) > 2:
                freq[s[l]]-=1
                if freq[s[l]] == 0:
                    del(freq[s[l]])
                l+=1
            ans = max(ans,r-l+1)      
        return ans