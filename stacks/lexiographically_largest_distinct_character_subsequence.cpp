// problem link : https://www.geeksforgeeks.org/lexicographically-largest-subsequence-containing-all-distinct-characters-only-once/
// This problem can be solved using stack as well, just replace string str with stack
#include<bits/stdc++.h>
using namespace std;

int main(){

string s; cin>>s;
int n = s.length();

vector<int>index(26);
vector<bool>visited(26, false);

for(int i = 0; i < n; i++){
    index[s[i]-'a']=i;
}
string str="";
for(int i = 0; i < n; i++){

if(visited[s[i]-'a']) continue;

while(str.length() > 0 && str.back() < s[i] && index[s[i]-'a'] > i){
    visited[str.back()-'a'] = false;
    str.pop_back();
}
 str.push_back(s[i]);
 visited[s[i]-'a'] = true;
}
cout<<str<<"\n";
}