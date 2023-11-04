// Problem Link : https://codeforces.com/problemset/problem/791/A

#include<bits/stdc++.h>
using namespace std;

int main(){
int a;
int b;
cin>>a>>b;
int count = 0;
while(a<=b){
a*=3;
b*=2;
count++;
}
cout<<count<<"\n";
return 0;
}