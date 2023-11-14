# problem link : https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result, subset = [],[]

        def backtrack(i):
            if i >=len(nums):
                result.append(subset.copy())
                return
            # include the character
            subset.append(nums[i])
            backtrack(i+1)
            # do not include the character
            subset.pop()
            backtrack(i+1)
        
        backtrack(0)
        return result
