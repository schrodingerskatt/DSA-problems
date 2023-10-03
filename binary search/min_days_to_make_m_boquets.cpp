// Question Link : https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/description/

//brute force approach 

class Solution {
public:
    int minDays(vector<int>& bloomDay, int m, int k) {

        if(bloomDay.size() < (long long)(k)*(long long)(m)) return -1;

        int min_bloom_day = INT_MAX;
        int max_bloom_day = INT_MIN;

        for(int i = 0; i < bloomDay.size();i++){
        min_bloom_day = min(bloomDay[i], min_bloom_day);
        max_bloom_day = max(bloomDay[i], max_bloom_day);
        }

        for(int i = min_bloom_day; i <= max_bloom_day; i++){
        
        int count = 0;
        int num_boq = 0;

        for(int j = 0; j < bloomDay.size(); j++){
        
        if(bloomDay[j] <= i){
            count++;
        }else{
        num_boq +=(count/k); 
        count = 0;
        }
        }
        num_boq += (count/k);
        if(num_boq >= m)
        return i;

        }
        return -1;
    }
};

//Optimal approach

