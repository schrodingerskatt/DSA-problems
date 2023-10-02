// Question Link : https://leetcode.com/problems/search-insert-position/

class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {

    int index = lower_bound(nums.begin(), nums.end(), target) - nums.begin();
    return index;
        
    }
};