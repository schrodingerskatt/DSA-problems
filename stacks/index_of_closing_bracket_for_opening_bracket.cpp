// Problem Link : https://www.geeksforgeeks.org/find-index-closing-bracket-given-opening-bracket-expression/

#include<bits/stdc++.h>
using namespace std;

int main(){

string expression; cin>>expression;
int index; cin>>index;

if(expression[index]!='[') {
cout<<"Give proper expression and index"<<"\n";
}else{

stack<char>st;
for(int i = index; i < expression.length(); i++){
if(expression[i]=='['){
st.push(expression[i]);
}
else if(expression[i]==']'){
        st.pop();
        if(st.empty()){
            cout<<"closing bracket found at index :"<<i<<"\n";
            break;
        }
    }
}
}
return 0;
}