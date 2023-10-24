// Problem Link : https://www.geeksforgeeks.org/find-maximum-difference-between-nearest-left-and-right-smaller-elements/

#include<bits/stdc++.h>
using namespace std;

class Solution{
    public:
   
int findMaxDiff(int A[], int n){
vector<int>left(n,0);
stack<int>st;
for(int i = 0; i < n; i++){
while(!st.empty() && st.top()>=A[i]){
st.pop();
}
if(!st.empty())
left[i] = st.top();
st.push(A[i]);
}
while(!st.empty()) st.pop();
vector<int>right(n,0);
for(int i = n-1; i>=0; i--){

while(!st.empty()&&st.top()>=A[i]){
st.pop();
}
if(!st.empty())
right[i] = st.top();
st.push(A[i]);
}
int ans = -1;
for(int i = 0; i < n; i++){
ans = max(ans, abs(left[i]-right[i]));
}
return ans;
    }
};
int main()
{
   int t;
   cin>>t;
   while(t--)
   {
   	int n;
   	cin>>n;
   	int a[n];
   	for(int i=0;i<n;i++)
   	cin>>a[i];
   	Solution ob;
   	cout<<ob.findMaxDiff(a,n)<<endl;
   }
    return 0;
}
