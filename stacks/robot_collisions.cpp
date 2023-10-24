#include<bits/stdc++.h>
using namespace std;

int main(){

int n; cin>>n;
vector<int>positions(n);
vector<int>healths(n);
string directions;

for(int i = 0; i < n; i++){
int p; cin>>p;
positions.push_back(p);
}
for(int i = 0; i < n; i++){
    int h; cin>>h;
    healths.push_back(h);
}
cin>>directions;

 vector<pair<int,pair<int,char>>>robo;
    stack<pair<int,pair<int,char>>>st;
    vector<int>result;
    
    for(int i = 0; i < n; i++){
        robo.push_back(make_pair(positions[i],make_pair(healths[i],directions[i])));
    }
    sort(robo.begin(),robo.end());
    st.push(make_pair(positions[0],make_pair(healths[0], directions[0])));

    for(int i = 1; i < n; i++){
    bool flag = true;

    while(!st.empty()&&st.top().second.second!=robo[i].second.second){
    if(st.top().second.first == robo[i].second.first){
    flag = false;
    st.pop();
    break;
    }
    else if(st.top().second.first > robo[i].second.first){
        st.top().second.first--;
        flag = false;
        break;
    }else{
        robo[i].second.first--;
        st.pop();
        st.push(make_pair(robo[i].first,make_pair(robo[i].second.first, robo[i].second.second)));
    }
    }
    if(flag!=false){
        st.push(make_pair(robo[i].first,make_pair(robo[i].second.first, robo[i].second.second)));
    }
    flag = true;
}

   if(st.empty()) return{};
   while(!st.empty()){
   result.push_back(st.top().second.first);
   st.pop();
   }
   reverse(result.begin(),result.end());

   return 0;

}