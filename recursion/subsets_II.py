# Problem Link : https://leetcode.com/problems/subsets-ii/description/

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        def dfs(i,ans):
            if i >= len(nums):
                result.append(ans.copy())
                return
            ans.append(nums[i])
            dfs(i+1,ans)
            ans.pop()
            while i+1 < len(nums) and nums[i]==nums[i+1]:
                i+=1
            dfs(i+1,ans)
        dfs(0,[])
        return result
        