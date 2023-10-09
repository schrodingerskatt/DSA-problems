// Problem Link : https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/description/

class Solution {
public:
    int longestPalindrome(vector<string>& words) {

        unordered_map<string,int>mp;
        for(int i = 0; i < words.size(); i++){
            mp[words[i]]++;
        }
        int length = 0;
        bool flag = false;
        for(string &word : words){
        
        string rev = word;
        reverse(word.begin(), word.end());

        if(word != rev){
            if(mp[word] > 0 && mp[rev] > 0){
                length +=4;
                mp[word]--;
                mp[rev]--;
            }
        }else{
             if(mp[word] > 1){
             mp[word]-=2;
             length+=4;
             }else if(mp[word] == 1 && flag == false){
                mp[word]--;
                length+=2;
                flag = true;
             }
            }
        }
        return length;
        }

        
    
};