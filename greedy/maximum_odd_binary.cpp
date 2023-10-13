// Problem Link : https://leetcode.com/problems/maximum-odd-binary-number/description/

class Solution {
public:
    string maximumOddBinaryNumber(string s) {
    
    int count_one = 0;
    int n = s.length();
    for(int i = 0; i < s.length(); i++){
    if(s[i] == '1')
    count_one++;
    }
    if(count_one > 0){
    s[n-1] = '1';
    count_one--;
    }

    for(int i = 0; i <count_one; i++){
     s[i] = '1';
    }
    for(int i = count_one; i < n-1; i++){
    s[i] = '0';
    }
    return s;  
    }
};