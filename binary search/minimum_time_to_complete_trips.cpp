// Questions : https://leetcode.com/problems/minimum-time-to-complete-trips/description/

// Binary Search Approach

class Solution {
public:
    long long minimumTime(vector<int>& time, int totalTrips) {
    int maxima = INT_MIN;

    for(int i = 0; i < time.size(); i++){
    maxima = max(maxima, time[i]);
    }
    int n = time.size();
    long long low = 1;
    long long high =1LL* maxima*totalTrips;

    while(low <= high){
    
    long long mid = low + (high - low)/2;
    long long trips = 0;
    for(int i = 0; i < time.size(); i++){
    trips += mid/time[i];
    }
    
    if(trips >= totalTrips) high = mid-1;
    else low = mid +1;
    }
    return low;    
    }
};