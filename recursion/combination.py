# Problem Link : https://leetcode.com/problems/combinations/description/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        ans = []
        def comb(x):
            if len(ans) == k:
                result.append(ans.copy())
                return 
            for i in range(x,n+1):
                ans.append(i)
                comb(i+1)
                ans.pop()
        comb(1)
        return result

        