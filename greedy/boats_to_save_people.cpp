// Problem Link : https://leetcode.com/problems/boats-to-save-people/

//  1. sort people according to their weights in ascending order
//  2. since, we can put atmost 2 people, try to make this 2 people weight maximum.
//  3. we can achieve this by adding lowest and the highest value
//  4. if the total weight is less than or equal to the limit value then we can increase our low and decrease high.
//  5. else weight at high was too big, and it might require separate boat for himself. so better to decrease our higher boundary.
//  6. keep on increasing the count, and return the count.

class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        
    sort(people.begin(), people.end());
    int low = 0;
    int high = people.size() - 1;
    int count = 0;
    while(low <= high){
    
    if(people[low] + people[high] <= limit){
    low++;
    high--;
    }
    else{
    high--;
    }
    count++;
    }
    return count;
    }
};