// Problem Link : https://codeforces.com/problemset/problem/110/A

#include<bits/stdc++.h>
using namespace std;

int main(){
string s; 
cin>>s;
int count_7=0;
int count_4=0;

for(int i = 0; i < s.length(); i++){
if(s[i]=='4') count_4++;
if(s[i]=='7') count_7++;
}
if(count_4+count_7 == 4 || count_4+count_7 == 7) cout<<"YES"<<"\n";
else cout<<"NO"<<"\n";
return 0;
}