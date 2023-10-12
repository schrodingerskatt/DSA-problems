// Problem Link : https://leetcode.com/problems/add-binary/description/

class Solution {
public:
    string addBinary(string a, string b) {
    string ans;
    int i = a.length() - 1;
    int j = b.length() - 1;
    int carry = 0;

    while( i >= 0 || j >= 0){
    int sum = carry;
    if( i>=0){
    sum += a[i]-'0';
    i--;
    }
    if(j >= 0){
    sum+=b[j]-'0';
    j--;
    }
    carry = sum/2;
    ans = to_string(sum%2) + ans;
    }
    if(carry)
    ans = '1' + ans;
    return ans;
    }
};