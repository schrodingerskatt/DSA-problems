# Problem Link : https://leetcode.com/problems/unique-paths/description/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        s = set()
        
        def backtrack(r,c):
       
            if r==m-1 and c==n-1:
                return 1
            if r > m or c >n or r < 0 or c < 0:
                return 0
            s.add((r,c))
            result = backtrack(r,c+1)+backtrack(r+1,c)
            s.remove((r,c))
            return result

        return backtrack(0,0)

 


