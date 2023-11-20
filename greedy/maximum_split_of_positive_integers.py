# Problem Link : https://leetcode.com/problems/maximum-split-of-positive-even-integers/description/

class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:

        if finalSum%2:
            return []
        else:
            res = []
            curSum = 0
            i = 2
            while curSum < finalSum:
                curSum+=i
                res.append(i)
                i+=2
            if curSum == finalSum:
                return res
            if curSum > finalSum:
                val = curSum-finalSum
                res.remove(val)
                return res

    

        
        