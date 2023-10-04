// Question Link : https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/description/

class Solution {
public:
    int smallestDivisor(vector<int>& nums, int threshold) {

    int maxima = INT_MIN;

    for(int i = 0; i < nums.size(); i++){
    maxima = max(nums[i], maxima);
    }
    
    int low = 1;
    int high = maxima;

    while(low <= high){
    
    int mid = low + (high - low)/2;
    long long sum = 0;
    for(int i = 0; i < nums.size(); i++){
    
    int val = ceil((double)(nums[i])/(double)(mid));
    sum += val;
    }
    if(sum <= threshold) high = mid - 1;
    else low = mid + 1;
    }
    return low;
    }
};