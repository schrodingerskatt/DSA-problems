// Problem Link : https://www.geeksforgeeks.org/length-of-the-longest-valid-substring/

#include<bits/stdc++.h>
using namespace std;

int main(){
string str; cin>>str;
stack<char>st;
st.push(str[0]);
for(int i = 1; i < str.length(); i++){
if(!st.empty() && st.top()=='(' && str[i] ==')'){
st.pop();
}
else{
st.push(str[i]);
}
}
cout<<str.length()-st.size()<<"\n";
return 0;
}