# Problem Link : https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def try_comb(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return 
            if i >= len(candidates) or total>target:
                return
            cur.append(candidates[i])
            try_comb(i,cur,total+candidates[i])
            cur.pop()
            try_comb(i+1,cur,total)

        try_comb(0,[],0)
        return res



        