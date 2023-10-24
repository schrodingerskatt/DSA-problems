// Problem Link : https://www.geeksforgeeks.org/delete-consecutive-words-sequence/

#include<bits/stdc++.h>
using namespace std;

int main(){

vector<string> str = { "ab", "aa", "aa", "bcd", "ab"}; 
stack<string>st;

for(int i = 0; i < str.size(); i++){

    if(st.empty()){
        st.push(str[i]);
    }
    else{
        string temp = st.top();
        if(temp == str[i])
        st.pop();
        else
        st.push(str[i]);
    }

}
return st.size();
}