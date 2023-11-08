# Problem Link : https://leetcode.com/problems/string-to-integer-atoi/description/

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0

        flag = False
        if s[0] == '-':
            flag = True
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

        ans = ""
        for char in s:
            if not char.isdigit():
                break
            else:
                ans += char

        if not ans:
            return 0

        ans = int(ans)
        if flag:
            if -ans < -2**31:
                return -2**31
            else:
                return -ans
        else:
            if ans > 2**31 - 1:
                return 2**31 - 1
            else:
                return ans