# Problem Link : https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        max_n = 2*n
        result = []
        def permute(i,curstr):
            if i == max_n:
                if self.isvalid(curstr):
                    result.append(curstr + '')
                    return
                else:
                    return 
            permute(i+1,curstr+'(')
            permute(i+1, curstr+')')

        permute(0,"")
        return result
    def isvalid(self, s):
        stack = []
        for i in range(0, len(s)):
            if s[i]==')' and len(stack)>0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(s[i])
        if len(stack)==0:
            return True
        return False
            

        