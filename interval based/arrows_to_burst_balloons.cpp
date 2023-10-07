// Problem Link : https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution {
public:
    int findMinArrowShots(vector<vector<int>>& points) {

    sort(points.begin(), points.end());
    vector<int>prev = points[0];
    int count = 1;
    for(int i = 1; i < points.size(); i++){
    
    if(points[i][0] > prev[1]){
    count++;
    prev = points[i];
    }else{
    prev[0] = points[i][0];
    prev[1] = min(points[i][1], prev[1]);
    }
    }
    return count; 
    }
};