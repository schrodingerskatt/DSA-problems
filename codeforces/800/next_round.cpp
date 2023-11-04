// Problem Link : https://codeforces.com/problemset/problem/158/A

#include<bits/stdc++.h>
using namespace std;

int main(){
int n;
int m;
cin>>n>>m;
int a[n];
for(int i = 0; i < n; i++){
int x; cin>>x;
a[i] = x;
}
int kth_score = a[m-1];
int cnt = 0;
for(int i = 0; i < n; i++){
if(a[i] >= kth_score && a[i]!=0)
cnt++;
}
cout<<cnt<<"\n";
return 0;
}