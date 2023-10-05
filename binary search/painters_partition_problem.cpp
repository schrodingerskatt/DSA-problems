// Question : https://www.codingninjas.com/studio/problems/painter-s-partition-problem_1089557

// brute force approach, as per striver 




#include <bits/stdc++.h>
using namespace std;

int countPainters(vector<int> &boards, int time) {
    int n = boards.size(); //size of array.
    int painters = 1;
    long long boardsPainter = 0;
    for (int i = 0; i < n; i++) {
        if (boardsPainter + boards[i] <= time) {
            //allocate board to current painter
            boardsPainter += boards[i];
        }
        else {
            //allocate board to next painter
            painters++;
            boardsPainter = boards[i];
        }
    }
    return painters;
}

int findLargestMinDistance(vector<int> &boards, int k) {
    int low = *max_element(boards.begin(), boards.end());
    int high = accumulate(boards.begin(), boards.end(), 0);

    for (int time = low; time <= high; time++) {
        if (countPainters(boards, time) <= k) {
            return time;
        }
    }
    return low;
}

int main()
{
    vector<int> boards = {10, 20, 30, 40};
    int k = 2;
    int ans = findLargestMinDistance(boards, k);
    cout << "The answer is: " << ans << "\n";
    return 0;
}



// binary search solution 


int findLargestMinDistance(vector<int> &boards, int k)
{
    int low = *max_element(boards.begin(), boards.end());
    int high = 0;
    
    for(int i = 0; i < boards.size(); i++){
        high += boards[i];
    }

    while(low <= high){
    
    int mid = low + (high - low)/2;
    long long total_time = 0;
    int painters = 1;
    for(int i = 0; i < boards.size(); i++){

    if(boards[i]+total_time <= mid){
    total_time += boards[i];
    }else{
    total_time = boards[i];
    painters++;
    }
    }
    if(painters > k) low = mid + 1;
    else high = mid - 1;
    }
    return low;
}