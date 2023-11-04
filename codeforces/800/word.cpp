// Problem Link : https://codeforces.com/problemset/problem/59/A

#include<bits/stdc++.h>
using namespace std;

int main(){
string s;
cin>>s;
int upper = 0;
int lower = 0;
for(int i =0; i < s.length(); i++){
if(isupper(s[i]))
upper++;
else
lower++;
}
string str;
if(upper > lower){
for(int i =0; i < s.length(); i++){
str+=toupper(s[i]);
}
}
else{
for(int i =0; i < s.length(); i++){
str+=tolower(s[i]);
}
}
cout<<str<<"\n";
return 0;
}