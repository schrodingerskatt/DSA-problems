# Problem Link : https://leetcode.com/problems/strobogrammatic-number/description/

class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        i = 0
        j = len(num)-1
        if len(num)==1:
            if num !='8' and num!='0' and num !='1':
                return False
            else:
                return True

        while i <= j:
            if num[i]=='6' and num[j]=='9' or num[i]=='8' and num[j]=='8' or num[i]=='0' and num[j]=='0' or num[i]=='1' and num[j]=='1' or num[i] == '9' and num[j] == '6':
                i+=1
                j-=1
                continue
            else:
                return False
        return True 
        