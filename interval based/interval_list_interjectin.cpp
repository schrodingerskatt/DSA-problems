// Problem Link : https://leetcode.com/problems/interval-list-intersections/

class Solution {
public:
    vector<vector<int>> intervalIntersection(vector<vector<int>>& firstList, vector<vector<int>>& secondList) {
        

    int n = firstList.size();
    int m = secondList.size();

    int i = 0;
    int j = 0;
    vector<vector<int>>ans;

    while(i < n && j < m){
    
    int pehla = max(firstList[i][0], secondList[j][0]);
    int dusra = min(firstList[i][1], secondList[j][1]);

    if(pehla <= dusra){
        ans.push_back({pehla, dusra});
    }
    if(firstList[i][1] < secondList[j][1])
    i++;
    else
    j++;
    }
    return ans;
    }
};