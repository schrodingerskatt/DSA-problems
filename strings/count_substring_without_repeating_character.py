# Problem Link : https://leetcode.com/problems/count-substrings-without-repeating-character/description/

class Solution:
    def numberOfSpecialSubstrings(self, s: str) -> int:
        st = set()
        i , j = 0, 0
        ans = 0

        while j < len(s):
            while s[j] in st:
                st.remove(s[i])
                i+=1
            
            st.add(s[j])
            ans = ans + (j-i)+1
            j+=1
        return ans
        