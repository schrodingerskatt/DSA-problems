# Problem Link : https://leetcode.com/problems/next-greater-numerically-balanced-number/description/

class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        while True:
            n+=1
            freq = defaultdict(int)
            num = n
            while num:
                d = num%10
                freq[d]+=1
                num = num//10 
            if all(k==v for k, v in freq.items()): return n
                
