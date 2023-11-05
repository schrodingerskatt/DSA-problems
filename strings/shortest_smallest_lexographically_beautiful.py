# problem link : https://leetcode.com/problems/shortest-and-lexicographically-smallest-beautiful-string/description/
# sliding window technique
class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)    
        L = []
        i = 0
        j = 0
        cnt = 0
        
        while j < n:
            if s[j] == '1':
                cnt += 1
            
            if cnt == k:
                while i <= j and s[i] == '0':
                    i += 1
                
                ans = s[i:j + 1]
                L.append(ans)
                
                i += 1
                cnt -= 1
            
            j += 1
        
        sorted_list = sorted(L, key=lambda x: (len(x), x))
        if sorted_list:
            return sorted_list[0]
        else:
            return ""
