// Problem Link : https://codeforces.com/problemset/problem/236/A

#include<bits/stdc++.h>
using namespace std;

int main(){
string s;
cin>>s;
set<char>st;
for(int i = 0; i < s.length(); i++)
st.insert(s[i]);
if(st.size()%2) cout<<"IGNORE HIM!"<<"\n";
else cout<<"CHAT WITH HER!"<<"\n";
return 0;
}