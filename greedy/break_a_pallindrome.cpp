// Problem Link : https://leetcode.com/problems/break-a-palindrome/description/

// Approach : 1. if the length of string is 1, then we can remove that character and return blank string.
//            2. we don't need to iterate the entire string, since its pallindrome the first half is same as second half.
//            3. 'a' is the smallest lexographic character, so if we replace the first character which is not 'a', by 'a'. it will be the smallest possible ans.
//            4. But, suppose if we have a case like 'aaaa', in this case we can replace last character by 'b'. i.e. -> 'aaab'.
//            5. we can encounter an edge case in 3. point for eg : if string is something like 'aabaa'.
//            6. since, 'b' is not 'a', and we might endup replacing 'b' by 'a'. but then the string would still remain pallindromic.
//            7. that's why we need to run our loop from 0 to n/2. if it reaches till n/2-1 this implys we are encountering situation like point 5 and 6.


class Solution {
public:
    string breakPalindrome(string palindrome) {
    
    int n = palindrome.size();
    if(n== 1) return "";
    
    for(int i = 0; i < n/2; i++){
        if(palindrome[i] != 'a'){
            palindrome[i] = 'a';
            return palindrome;
        }
        
    }
   
    palindrome[n-1] = 'b';
    return palindrome; 
    }
};