// Problem Link : https://leetcode.com/problems/gas-station/description/

// Approach : https://www.youtube.com/watch?v=lJwbPZGo05A

class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {

    int n = cost.size();
    int total_gas = 0, total_cost = 0;
    
    for(int i = 0; i < n; i++){
    
    total_gas += gas[i];
    total_cost += cost[i];
    }

    if(total_cost > total_gas) return -1;

    int total = 0;
    int start = 0;

    for(int i = 0; i < n; i++){
      
      total += (gas[i] - cost[i]);

       if(total < 0){
           total = 0;
           start = i + 1;
       }

    }
    return start;
}

};