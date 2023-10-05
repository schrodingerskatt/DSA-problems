// Question Link : https://leetcode.com/problems/car-pooling/description/

class Solution {
public:
    bool carPooling(vector<vector<int>>& trips, int capacity) {

    vector<int>totalcapacity(1001);

    for(vector v : trips){
    int from = v[1];
    int to = v[2];
    int count = v[0];
    totalcapacity[to] -=count;
    totalcapacity[from] +=count;
    }
    int sum = 0;
    for(int i = 0; i < totalcapacity.size(); i++){
    sum += totalcapacity[i];
    if(sum > capacity) return false;
    }
    return true;
    }
};