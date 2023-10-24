// Problem Link : https://www.geeksforgeeks.org/remove-characters-from-the-first-string-which-are-present-in-the-second-string/

// naive approach

//{ Driver Code Starts
// Initial template for C++
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// User function template for c++
class Solution {
  public:
    string removeChars(string string1, string string2) {
        
        map<char,int>mp;
        for(int i = 0; i < string2.length(); i++){
            mp[string2[i]]++;
        }
        string ans ="";
        for(int i = 0; i < string1.length(); i++){
            if(mp.find(string1[i])==mp.end()){
                ans+=string1[i];
            }
        }
    return ans;
    }
};


int main() {
    int t;
    cin >> t;
    while (t--) {
        string string1,string2;
        cin >> string1; 
        cin >> string2;
        Solution ob;
        cout << ob.removeChars(string1,string2) << endl;
    }
    return 0;
}

