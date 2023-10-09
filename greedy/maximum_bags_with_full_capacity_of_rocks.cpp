// Problem Link : https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/

class Solution {
public:
    int maximumBags(vector<int>& capacity, vector<int>& rocks, int additionalRocks) {

    int n = capacity.size();
    vector<int>max_required(n);

    for(int i = 0; i < n; i++){
    max_required[i] = capacity[i] - rocks[i];
    }
    sort(max_required.begin(), max_required.end());
    int count = 0;

    for(int i = 0; i < n; i++){

    if(max_required[i] == 0) count++;
    else{
    if(max_required[i] <= additionalRocks){
    additionalRocks -= max_required[i];
    count++;
    }
    }
    }
    return count;  
    }
};