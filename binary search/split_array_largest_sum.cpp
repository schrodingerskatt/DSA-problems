// Question Link : https://leetcode.com/problems/split-array-largest-sum/

class Solution {
public:
    int splitArray(vector<int>& nums, int k) {
    
    long long low = *max_element(nums.begin(),nums.end());
    int high = 0;
    for(int i = 0; i < nums.size(); i++){
        high+= nums[i];
    }

    while(low < high){
    
    long long mid = low + (high - low)/2;

    long long sum = 0;
    int count = 1;

    for(int i = 0; i < nums.size(); i++){
    
    if(nums[i] + sum <= mid){
    sum += nums[i];
    }else{
    sum = nums[i];
    count++;
    }
    }
    if(count > k) low = mid + 1;
    else high = mid;
    }
    return high;
    }
};