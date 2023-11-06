# Problem Link : https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-ii/description/

class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        # we can replace even position with even and odd with odd
        
        # selecting every even character from s1
        s1_even = s1[::2]
        # selecting every even character from s2
        s2_even = s2[::2]
        # selecting every odd character from s1
        s1_odd = s1[1::2]
        # selecting every odd character from s2
        s2_odd = s2[1::2]
        if sorted(s1_even) == sorted(s2_even) and sorted(s1_odd) == sorted(s2_odd):
            return 1
        else:
            return 0




        