// Problem Link : https://codeforces.com/problemset/problem/112/A

#include<bits/stdc++.h>
using namespace std;

int main(){
string x; 
string y;
cin>>x>>y;
string x_s;
string y_s;
for(int i = 0; i < x.length(); i++){
x_s+=tolower(x[i]);
y_s+=tolower(y[i]);
}
if(x_s==y_s) cout<<"0"<<"\n";
else if(x_s < y_s) cout<<"-1"<<"\n";
else cout<<"1"<<"\n";
return 0;
}