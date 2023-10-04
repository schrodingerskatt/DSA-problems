// Question Link : https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/


// Brute force approach

class Solution {
public:
    int findKthPositive(vector<int>& arr, int k) {

    int n = arr.size();
    int num = 1;
    int i = 0;

    while( i < n && k > 0){
    
    if(arr[i] == num){
    i++;
    }else{
    k--;
    }
    num++;
    }
    while(k--) {
        num++;
    }
        
    return num-1;
    }
};

// Binary Search Solution

class Solution {
public:
    int findKthPositive(vector<int>& arr, int k) {
    int n = arr.size();
    int low = 0;
    int high = n-1;

    while(low <= high){
    
    int mid = low + (high - low)/2;

    if(arr[mid] - (mid+1) < k){
        low = mid + 1;
    }else{
        high = mid - 1;
    }
    }
    return low+k;
        
    }
};