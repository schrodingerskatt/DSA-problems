# Problem Link : https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        letters = {"2": "abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno","7": "pqrs", "8": "tuv", "9":"wxyz"}

        def backtrack(i, curstr):
            if len(curstr) == len(digits):
                res.append(curstr)
                return 
            for char in letters[digits[i]]:
                backtrack(i+1, curstr+char)
        if digits:
            backtrack(0,"")
        return res

        