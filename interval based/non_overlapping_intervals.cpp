// Questions : https://leetcode.com/problems/non-overlapping-intervals/

class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {

        sort(intervals.begin(), intervals.end());

        vector<int> val = intervals[0];
        int count = 0;
        for(int i = 1; i < intervals.size(); i++){
        
        if(intervals[i][0] < val[1])
        count++;
        else
        val = intervals[i];
        }
        return count;
    }
};