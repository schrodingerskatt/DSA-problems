// Problem Link : https://www.geeksforgeeks.org/maximum-product-of-indexes-of-next-greater-on-left-and-right/

#include<bits/stdc++.h>
using namespace std;

int main(){

int n; cin>>n;
int arr[n];
for(int i = 0; i < n; i++) cin>>arr[i];
vector<int>left(n,0);
stack<int>st;
for(int i = 0; i < n; i++){
while(!st.empty() && arr[st.top()]<=arr[i]){
st.pop();
}
if(!st.empty())
left[i] = st.top();
st.push(i);
}
while(!st.empty()) st.pop();
vector<int>right(n,0);
for(int i = n-1; i>=0; i--){
while(!st.empty()&&arr[st.top()]<=arr[i]){
st.pop();
}
if(!st.empty())
right[i] = st.top();
st.push(i);
}
int ans = INT_MIN;
for(int i = 0; i < n; i++){
int val = (left[i]+1)*(right[i]+1);
ans = max(ans, val);
}
cout<<ans<<"\n";
return 0;
}
