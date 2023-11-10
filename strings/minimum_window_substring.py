# Problem Link : https://leetcode.com/problems/minimum-window-substring/description/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        freq, window = {},{}
        for w in t:
            freq[w] = 1+freq.get(w,0)
        l = 0
        pointers = [-1,-1]
        min_len = float('inf')
        have, need = 0, len(freq)
        for r in range(len(s)):
            window[s[r]] = 1+window.get(s[r],0)
            if s[r] in freq and window[s[r]]==freq[s[r]]:
                have+=1
            while have == need:
                if (r-l+1) < min_len:
                    pointers = [l,r]
                    min_len = r-l+1
                window[s[l]]-=1
                if s[l] in freq and window[s[l]] < freq[s[l]]:
                    have-=1
                l+=1
        l, r = pointers
        return s[l:r+1] if min_len != float('inf') else ""