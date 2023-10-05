// Question Link : https://www.codingninjas.com/studio/problems/allocate-books_1090540?utm_source=youtube&utm_medium=affiliate&utm_campaign=codestudio_Striver_BinarySeries&leftPanelTab=0

// brute force approach, as per striver solution

#include <bits/stdc++.h>
using namespace std;

int countStudents(vector<int> &arr, int pages) {
    int n = arr.size(); //size of array.
    int students = 1;
    long long pagesStudent = 0;
    for (int i = 0; i < n; i++) {
        if (pagesStudent + arr[i] <= pages) {
            //add pages to current student
            pagesStudent += arr[i];
        }
        else {
            //add pages to next student
            students++;
            pagesStudent = arr[i];
        }
    }
    return students;
}

int findPages(vector<int>& arr, int n, int m) {
    //book allocation impossible:
    if (m > n) return -1;

    int low = *max_element(arr.begin(), arr.end());
    int high = accumulate(arr.begin(), arr.end(), 0);

    for (int pages = low; pages <= high; pages++) {
        if (countStudents(arr, pages) == m) {
            return pages;
        }
    }
    return low;
}

int main()
{
    vector<int> arr = {25, 46, 28, 49, 24};
    int n = 5;
    int m = 4;
    int ans = findPages(arr, n, m);
    cout << "The answer is: " << ans << "\n";
    return 0;
}

// Binary Search Approach

int findPages(vector<int>& arr, int n, int m) {

    if(n < m) return -1;
    
    int low = *max_element(arr.begin(), arr.end());
    int high = 0;
    for(int i = 0; i < arr.size(); i++){
        high += arr[i];
    }

    while(low <= high){
    
    int mid = low + (high - low)/2;

    long long students = 1;
    long long max_pages = 0;

    for(int i = 0; i < arr.size(); i++){
    
    if(max_pages + arr[i] <= mid){
    max_pages+=arr[i];
    }else{
    students++;
    max_pages = arr[i];
    }
    }
    if(students > m) low = mid + 1;
    else high = mid - 1;
    }

    return low;
}