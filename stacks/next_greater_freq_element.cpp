// Problem Link : https://www.geeksforgeeks.org/next-greater-frequency-element/

#include <bits/stdc++.h>
#define N 10000
using namespace std;

class Solution{
public:
    vector<int> print_next_greater_freq(int arr[],int n)
    {
    unordered_map<int, int> freq;
    vector<int> result(n, -1);
    stack<int> st;

    for (int i = 0; i < n; i++) {
        freq[arr[i]]++;
    }

    for (int i = n - 1; i >= 0; i--) {
        while (!st.empty() && freq[arr[i]] >= freq[st.top()]) {
            st.pop();
        }

        if (!st.empty()) {
            result[i] = st.top();
        }

        st.push(arr[i]);
    }
    return result;
    }
};


int main()
{
    int arr[N];
    
    int t;
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        
        for(int i=0; i<n; i++)
            cin>>arr[i];
        
        Solution ob;
        vector<int> ans=ob.print_next_greater_freq(arr,n);
        for(auto x:ans){
            cout<<x<<" ";
        }
        cout << endl;
    }
	return 1;
}
