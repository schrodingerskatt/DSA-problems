// Problem Link : https://www.geeksforgeeks.org/the-celebrity-problem/

#include<bits/stdc++.h>
using namespace std;
class Solution 
{
    public:
    int celebrity(vector<vector<int> >& M, int n) 
    {
        
    stack<int>st;
    for(int i = 0; i < n; i++){
        st.push(i);
    }
    while(st.size()>=2){
    
    int second = st.top();
    st.pop();
    int first = st.top();
    st.pop();
    
    if(M[first][second]){
        st.push(second);
    }else{
        st.push(first);
    }
    }
    int pos = st.top();
    for(int i = 0; i < n; i++){
    if(i!=pos){
    if(M[i][pos]==0||M[pos][i]==1)
    return -1;
    }
    }
    return pos;
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
        vector<vector<int> > M( n , vector<int> (n, 0));
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<n;j++)
            {
                cin>>M[i][j];
            }
        }
        Solution ob;
        cout<<ob.celebrity(M,n)<<endl;

    }
}