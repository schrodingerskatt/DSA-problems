# Problem Link : https://leetcode.com/problems/shortest-string-that-contains-three-strings/description/

class Solution:

    def merge(self, s1, s2):
        if s2 in s1:
            return s1
        for i in range(len(s1)):
            if s2.startswith(s1[i:]):
                return s1[:i]+s2
        return s1+s2

    def minimumString(self, a: str, b: str, c: str) -> str:

        L = []
        L.append(self.merge(self.merge(a,b),c))
        L.append(self.merge(self.merge(b,a),c))
        L.append(self.merge(self.merge(b,c),a))
        L.append(self.merge(self.merge(c,b),a))
        L.append(self.merge(self.merge(a,c),b))
        L.append(self.merge(self.merge(c,a),b))
        L = sorted(L, key = lambda x: (len(x),x))
        return L[0]
        
