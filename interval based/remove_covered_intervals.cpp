// Question Link : https://leetcode.com/problems/remove-covered-intervals/

class Solution {
public:

    static bool cmp(vector<int>& v1, vector<int>& v2) {
        if(v1[0] == v2[0])
            return v1[1] > v2[1];
        return v1[0]<v2[0];
    }
    int removeCoveredIntervals(vector<vector<int>>& intervals) {

         if(intervals.size() == 0 || intervals.size() == 1)
            return intervals.size();

    sort(intervals.begin(), intervals.end(), cmp);

    vector<vector<int>>start;
    start.push_back(intervals[0]); 
    int count = 0;
    for(int i = 1; i < intervals.size(); i++){
    
    if(start[0][0]<= intervals[i][0] && start[0][1] >= intervals[i][1])
        count++;
    else{
        start[0][0] = intervals[i][0];
        start[0][1] = intervals[i][1];
    }

    }
    return intervals.size()-count;       
    }
};