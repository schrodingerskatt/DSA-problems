# Problem Link : https://leetcode.com/problems/subarray-sum-equals-k/description/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hmp = {0:1}
        count, total = 0,0
        for num in nums:
            total+=num
            if total-k in hmp:
                count+=hmp[total-k]
            hmp[total]=1+hmp.get(total,0)
        return count

'''
[1,-1,1,1] and k = 2
we have to find count of all subarrays whose sum == k. 
let's take an example of this series a,b,c,d,e,f...
here c+d+e+f = k, the only extra values here are a,b
total sum = a+b+k
how would we know that starting point of k sum is c ? To find this we will keep on adding numbers and
will check whether it is equal to k, if not we will check whether the sum-k has occured before. In the above
example we will first store a then a+b, then a+b+c....in the hashmap. but when the sum will reach
a+b+c+d+e+f and we will subtract k from it we will get a+b, this sum has already occured before, this
implies [c,d,e,f] is equal to k. every time we encountered a previously occured sum we will keep on increasing
the count, and will finally print it at the end.
'''