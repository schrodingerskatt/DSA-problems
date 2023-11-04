// Problem Link : https://codeforces.com/problemset/problem/282/A

#include<bits/stdc++.h>
using namespace std;

int main(){
int t;
cin>>t;
int cnt=0;
while(t--){
string s;
cin>>s;
if(s[0]=='+'|| s[2]=='+')
cnt+=1;
else
cnt-=1;
}
cout<<cnt<<"\n";
return 0;
}