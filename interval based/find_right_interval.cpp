// Problem Link : https://leetcode.com/problems/find-right-interval/

//brute force approach

class Solution {
public:
    vector<int> findRightInterval(vector<vector<int>>& intervals) {

    vector<int>rightinterval;

    for(int i = 0; i < intervals.size(); i++){
    
    int index = -1;
    int ans = INT_MAX;

    for(int j = 0; j < intervals.size(); j++){
    
    if(intervals[i][1] <= intervals[j][0] && intervals[j][0] < ans){
    ans = intervals[j][0];
    index = j;
    }
    }
    rightinterval.push_back(index);
    }
    return rightinterval;
    }
};

// Optimized approach using binary search

class Solution {
public:
    vector<int> findRightInterval(vector<vector<int>>& intervals) {

    map<int, int>start_points;
    int n = intervals.size();

    for(int i = 0; i<n; i++) {
    start_points[intervals[i][0]] = i;
    }
  
    vector<int> result(n, -1);

    for(int i = 0; i < intervals.size(); i++){
    
    auto higher_start_point = start_points.lower_bound(intervals[i][1]);

    if(higher_start_point != start_points.end()){
    result[i] = higher_start_point->second;
    }
 
    }
    return result;  
    }
};