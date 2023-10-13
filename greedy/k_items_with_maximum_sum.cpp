// Problem Link : https://leetcode.com/problems/k-items-with-the-maximum-sum/description/

class Solution {
public:
    int kItemsWithMaximumSum(int numOnes, int numZeros, int numNegOnes, int k) {
        
    if(k <= numOnes)
    return k;
    else{
    if(numOnes + numZeros >= k)
    return numOnes;
    else{
    int negs = k - (numOnes+numZeros);
    return numOnes - negs;
    }
    }
    return 0;
    }
};