// Problem Link : https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/description/

// Approach : 1. If a count is divisible by 3, then we it is of form 3k, it means it will give us minimum ans if we divide by 3.
//            2. But what if it is not divisible by 3. it means it is form 3k+1 or 3k+2.
//            3. for eg : if it is 10 then => 3,3,3,1 => here, we are getting 1 left so not possible.
//            4. but we can also write it as 10 => 3,3,2,2 => possible (10/3) + 1
//            5. for 3k+2 i.e. 11 => 3,3,3,2 => (11/3) + 1
//            6. In short it is possible for all cases except when the count is 1.


class Solution {
public:
    int minimumRounds(vector<int>& tasks) {
    map<int,int>mp;

    for(int i = 0; i < tasks.size(); i++){
    mp[tasks[i]]++;
    }
    int cnt = 0;
    for(auto x : mp){
    if(x.second == 1) return -1;
    else if (x.second % 3 == 0)
    cnt += x.second/3;
    else
    cnt += (x.second/3)+1;
    }  
    return cnt;
    }
};