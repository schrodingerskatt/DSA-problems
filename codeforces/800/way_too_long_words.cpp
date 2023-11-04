// Problem Link : https://codeforces.com/problemset/problem/71/A

#include<bits/stdc++.h>
using namespace std;

int main(){
long long t;
cin>>t;
while(t--){
string s; cin>>s;
int len = s.length();
if(len <= 10) cout<<s<<"\n";
else{
cout<<s[0]+to_string(len-2)+s[len-1]<<"\n";
}
}
return 0;
}