// Problem Link : https://leetcode.com/problems/earliest-possible-day-of-full-bloom/description/
// Video : https://www.youtube.com/watch?v=kqOVhPfrP_I&list=PLpIkg8OmuX-J8_n8Vy9P9I3KvyDcPMzRU&index=6


class Solution {
public:
    int earliestFullBloom(vector<int>& plantTime, vector<int>& growTime) {

    int n = plantTime.size();

    vector<pair<int,int>>bloom(n);

    for(int i = 0; i < n; i++){
    bloom[i] = {plantTime[i], growTime[i]};
    }

    auto lambda = [](pair<int,int>&P1, pair<int,int>&P2){
      return P1.second > P2.second;
    };

    sort(bloom.begin(), bloom.end(), lambda);    

    int prev_plant_day = 0;
    int max_bloom_day = 0;
   

    for(int i = 0; i < n; i++){
    prev_plant_day += bloom[i].first;
    int bloom_day = prev_plant_day + bloom[i].second;
    max_bloom_day = max(max_bloom_day, bloom_day);
    }
    return max_bloom_day;
    }
};