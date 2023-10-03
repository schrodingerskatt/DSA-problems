// Question Link : https://leetcode.com/problems/koko-eating-bananas/

// brute force approach

class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {

    int max_val = INT_MIN;

    for(int i = 0; i <piles.size();i++){
    max_val = max(max_val,piles[i]);
    }

    for(int i = 1; i <= max_val; i++){
    int banana = i;
    long long hours = 0;
    for(int i = 0; i < piles.size();i++){
    hours += ceil((double)(piles[i])/(double)(banana));
    }
    if(hours <= h) return i;
    }
    return -1;
    }
};

// Optimal approach using binary search

class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {

    int max_hr = INT_MIN;
    for(int i = 0; i <piles.size(); i++){
        max_hr = max(max_hr, piles[i]);
    }

    int low = 1, high = max_hr;

    while(low <= high){
    int mid = low + (high - low)/2;
    long long sum = 0;
    for(int i = 0; i < piles.size(); i++){
    sum += ceil((double)(piles[i])/(double)(mid));
    }
    if (sum <= h) high = mid - 1;
    else low = mid + 1;
    }
    
    return low; // there will be a time when high pointer will move ahead of low and ans will be at low index.
    }
};