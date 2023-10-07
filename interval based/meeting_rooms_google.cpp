// Question Link : https://leetcode.com/discuss/interview-question/613816/Google-or-Onsite-or-Meeting-Rooms-3


// This code is not tested. If you found some edge case in this approach, let me know.

#include<bits/stdc++.h>
using namespace std;

int main(){

vector<vector<int>>calendar{{1,2},{4,5},{8,10}};
vector<vector<int>>queries{{4,5},{5,6}};
int rooms = 1;
sort(calendar.begin(), calendar.end());
sort(queries.begin(), queries.end());

map<int,int>mp;
for(int i = 0; i < calendar.size(); i++){
mp[calendar[i][0]]++;
mp[calendar[i][1]]--;
}
int maxima = INT_MIN;
for(int i = 0; i < calendar.size(); i++){
maxima = max(maxima, calendar[i][1]);
}
vector<bool>output;
int ans = 0;
vector<int>storage(maxima+1, 0);
for(auto x: mp){
ans+=x.second;
storage[x.first] = ans;
}
for(int i = 0; i < queries.size();i++){
if(storage[queries[i][0]] < rooms)
output.push_back(true);
else
output.push_back(false);
}
for(int i : output){
cout<<i<<" ";
}
return 0;
}