// Problem : https://practice.geeksforgeeks.org/problems/stock-span-problem-1587115621/1
#include<bits/stdc++.h>
using namespace std;

class Solution
{
    public:
    vector <int> calculateSpan(int price[], int n)
    {
       stack<int>st;
       vector<int>ans;
       
       for(int i = 0; i < n; i++){
          
          while(!st.empty() && price[st.top()] <= price[i]){
              st.pop();
          }
          if(st.empty())
          ans.push_back(i+1);
          else ans.push_back(i-st.top());
          st.push(i);
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
		int i,a[n];
		for(i=0;i<n;i++)
		{
			cin>>a[i];
		}
		Solution obj;
		vector <int> s = obj.calculateSpan(a, n);
		
		for(i=0;i<n;i++)
		{
			cout<<s[i]<<" ";
		}
		cout<<endl;
	}
	return 0;
}

