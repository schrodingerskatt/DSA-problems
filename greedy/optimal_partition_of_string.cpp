// Problem Link : https://leetcode.com/problems/optimal-partition-of-string/description/

class Solution {
public:
    int partitionString(string s) {
        
    unordered_set<int>st;
    int count = 1;

    for(int i = 0; i < s.length(); i++){
    
    if(st.count(s[i])){
    count++;
    st.clear();
    }
    st.insert(s[i]);
    }
    return count;
    }
};