// Problem Link : https://www.geeksforgeeks.org/evaluation-of-postfix-expression/

int evaluate_infix(string exp){


stack<int>st;
for(int i = 0; i < exp.length(); i++){
    if(digit[exp[i]]){
        st.push(exp[i]-'0');
    }
    else{
        int second = st.top();
        st.pop();
        int first = st.top();
        st.pop();
        if(exp[i]=='+')
        st.push(first+second);
        else if(exp[i]=='-')
        st.push(first-second);
        else if(exp[i]=='*')
        st.push(first*second);
        else
        st.push(first/second);
    }
}
return st.top();
}