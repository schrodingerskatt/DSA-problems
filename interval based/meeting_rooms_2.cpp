// Question Link : https://www.interviewbit.com/problems/meeting-rooms/

// Hash map approach

int Solution::solve(vector<vector<int> > &A) {
    
map<int,int>mp;

for(int i = 0; i < A.size(); i++){
    mp[A[i][0]]++;
    mp[A[i][1]]--;
}
int count = INT_MIN;
int ans = 0;
for(auto x : mp){
ans+= x.second;
count = max(count,ans);
}
return count;
}


// priority queue approach

int Solution::solve(vector<vector<int> > &A) {
sort(A.begin(),A.end());
priority_queue <int, vector<int>, greater<int>> pq;

pq.push(A[0][1]);
int ans = INT_MIN;
for(int i = 1; i < A.size(); i++){
if(pq.top() > A[i][0]){
}else{
pq.pop();
}
pq.push(A[i][1]);
if(ans < (int)pq.size())
ans = (int)pq.size();
}
return ans;
}
