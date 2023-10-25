// Problem link : https://www.geeksforgeeks.org/maximum-people-a-person-can-see-while-standing-in-a-line-in-both-direction/

#include<bits/stdc++.h>
using namespace std;

int main(){

int n; cin>>n;
int heights[n];
for(int i = 0; i < n; i++) cin>>heights[i];

vector<int>left_sight(n),right_sight(n);
stack<int>st;

for(int i = 0; i < n; i++){

  while(!st.empty() && heights[st.top()] < heights[i])
  st.pop();
  
  if(st.empty()) left_sight[i] = -1;
  else left_sight[i] = st.top();
  st.push(i);
}

while(!st.empty()) st.pop();

for(int i = n-1; i >=0; i--){

 while(!st.empty() && heights[st.top()] < heights[i])
 st.pop();
 
 if(st.empty()) right_sight[i] = n;
 else right_sight[i] = st.top();
 st.push(i);
}

int ans = 0;

for(int i = 0; i < n; i++){
    ans = max(ans, right_sight[i]-left_sight[i]-1);
}
cout<<ans<<"\n";
return 0;
}