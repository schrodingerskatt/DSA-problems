# Problem Link : https://leetcode.com/problems/one-edit-distance/description/

class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if abs(len(s) - len(t)) > 1:
            return False
        if s == "" and t == "" or s==t:
            return False
        i, j = 0, 0
        count = 0

        while i < len(s) and j < len(t):
            if s[i] != t[j]:
                count += 1
                if count > 1:
                    return False

                # Check for insertion, deletion, or substitution
                if len(s) > len(t):
                    i += 1
                elif len(t) > len(s):
                    j += 1
                else:
                    i += 1
                    j += 1

            else:
                i += 1
                j += 1

        # Handle the case where one string is longer than the other by exactly one character
        if count <=1:
            return True
        else:
            return False
