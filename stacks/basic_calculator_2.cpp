// Problem Link : https://leetcode.com/problems/basic-calculator-ii/description/

// Stack Approach

class Solution {
public:
    int calculate(string s) {

    int len = s.length();
    if(len == 0) return 0;
    stack<int>st;
    int currentnumber = 0;
    char currentop = '+';

    for(int i = 0; i < s.length(); i++){
     char ch = s[i];
     if(isdigit(ch)){
         currentnumber = currentnumber*10+(ch-'0');
     }
     if(!isdigit(ch)&&!iswspace(ch)||i==len-1){
        
        if(currentop == '+'){
            st.push(currentnumber);
        }
        else if(currentop == '-'){
            st.push(-currentnumber);
        }
        else if(currentop == '*'){
            int top = st.top();
            st.pop();
            st.push(top*currentnumber);
        }
        else if(currentop == '/'){
            int top = st.top();
            st.pop();
            st.push(top/currentnumber);
        }
     currentop = ch;
     currentnumber = 0;
     }
    }
    int sum = 0;
    while(!st.empty()){
        sum+=st.top();
        st.pop();
    }
    return sum;
    }
};

// String Approach

class Solution {
public:
    int calculate(string s) {
        
        int currentnumber = 0, lastnumber = 0, result = 0;
        char sign = '+';

        for(int i = 0; i < s.length(); i++){
        
        char ch = s[i];
        if(isdigit(ch)){
        currentnumber = currentnumber*10+(ch-'0');
        }
        if(!isdigit(ch)&&!iswspace(ch)||i==s.length()-1){
            if(sign == '+'||sign == '-'){
                result += lastnumber;
                lastnumber = (sign == '+') ? currentnumber : -currentnumber;
            }
            else if(sign == '*'){
                lastnumber = lastnumber*currentnumber;
            }
            else if(sign == '/'){
                lastnumber = lastnumber/currentnumber;
            }
        sign = ch;
        currentnumber = 0;
        }
        }
    result += lastnumber;
    return result;
    }
};