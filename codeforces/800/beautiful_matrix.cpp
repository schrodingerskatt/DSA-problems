//Problem Link : https://codeforces.com/problemset/problem/263/A

#include<bits/stdc++.h>
using namespace std;

int main(){

int m[5][5];
int pos_i = -1;
int pos_j = -1;
for(int i = 0; i < 5; i++){
for(int j = 0; j < 5; j++){
int val;
cin>>val;
if(val == 1){
pos_i = i;
pos_j = j;
}
m[i][j] = val;
}
}
cout<<abs(pos_i-2)+abs(pos_j-2)<<"\n";
return 0;
}