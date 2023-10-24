// Problem Link : https://www.geeksforgeeks.org/minimize-length-by-removing-subsequences-forming-valid-parenthesis-from-a-given-string/

#include<bits/stdc++.h>
using namespace std;

int main(){
string str; cin>>str;
int roundb = 0;
int squareb = 0;
stack<char>roundb_stk;
stack<char>squareb_stk;

for(int i = 0; i < str.length(); i++){
if(str[i]=='(')
roundb_stk.push(str[i]);
else if(roundb_stk.size() >0 && str[i]==')'){
roundb_stk.pop();
roundb++;
}
else if(str[i]=='[')
squareb_stk.push(str[i]);
else{
    if(squareb_stk.size() > 0 && str[i] ==']'){
    squareb_stk.pop();
    squareb++;
    }
}
}
cout<<str.length()-2*(squareb+roundb)<<"\n";
return 0;
}