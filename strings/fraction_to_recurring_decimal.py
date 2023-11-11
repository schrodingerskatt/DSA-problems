# Problem Link : https://leetcode.com/problems/fraction-to-recurring-decimal/description/

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        ans = []
        if (denominator < 0) ^ (numerator < 0):
            ans.append('-')
        ans.append(str(abs(numerator)//abs(denominator)))
        if abs(numerator)%abs(denominator) == 0:
            return "".join(ans)
        else:
            ans.append('.')
            r = abs(numerator)%abs(denominator)
            hmp = {}
            while r != 0:
                if r in hmp:
                    idx = hmp[r]
                    ans.insert(idx, '(')
                    ans.append(')')
                    break
                else:
                    hmp[r]=len(ans)
                    r = r*10
                    q = r//abs(denominator)
                    r = r%abs(denominator)
                    ans.append(str(q))
        return "".join(ans)

        
        