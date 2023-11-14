# Problem Link : https://leetcode.com/problems/permutations/description/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(curstr,i,j):
            if i == j:
                res.append(curstr.copy())
                return
            for l in range(i,j):
                nums[l],nums[i]=nums[i],nums[l]
                dfs(curstr,i+1,j)
                nums[i],nums[l]=nums[l],nums[i]
        dfs(nums,0,len(nums))
        return res

        