// Question Link : https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

class Solution {
public:

    int binary_search(vector<int>&nums, int search, bool flag){
    
    int low = 0, high = nums.size() - 1;
    int pos = -1;
    while(low <= high){
    
    int mid = low+(high-low)/2;

    if(nums[mid] > search){
    high = mid -1;
    }
    else if(nums[mid] < search){
    low = mid + 1;
    }
    else{
    pos = mid;
    if(flag){
    high = mid-1;
    }
    else{
    low = mid + 1;
    }
    }
    }
    return pos;
    }