// Problem Link : https://leetcode.com/problems/maximum-ice-cream-bars/

class Solution {
public:
    int maxIceCream(vector<int>& costs, int coins) {

    sort(costs.begin(), costs.end());
    int max_icecream = 0;
    for(int i = 0; i < costs.size(); i++){
    if(costs[i] <= coins){
        coins -= costs[i];
        max_icecream++;
    }else{
    break;
    }
    }
    return max_icecream;
    }
};