// Problem Link : https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/

class Solution {
public:
    int minDeletions(string s) {

    int freq[26] = {0};
    for(int i = 0; i < s.size(); i++){
    freq[s[i]-'a']++;
    }
    sort(freq, freq+26, greater<int>());
    int count = 0;
    for(int i = 0; i < 25; i++){
    if(freq[i+1] >= freq[i]){
    int prev = freq[i+1];
    freq[i+1] = max(freq[i] - 1, 0);
    count += prev - freq[i+1];
    }
    }
    return count;   
    }
};