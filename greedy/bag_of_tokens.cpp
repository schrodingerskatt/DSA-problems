// Problem Link : https://leetcode.com/problems/bag-of-tokens/

// Approach : 1. when it comes to loosing power and increasing score, we will give min. value of power.
//            2. when it comes to gaining power and decreassing score, we will take max. value of power.
//            3. sort the array, loose power from begininig of array, and take power from end.
//            4. return the maximum value of power.

class Solution {
public:
    int bagOfTokensScore(vector<int>& tokens, int power) {

    int i = 0;
    int j = tokens.size()-1;
    sort(tokens.begin(), tokens.end());
    int maxScore = 0;
    int score = 0;
    while(i <= j){
    
    if(tokens[i] <= power){
    power -= tokens[i];
    score++;
    i++;
    maxScore = max(maxScore, score);
    }  
    else if(score >= 1){
    power += tokens[j];
    j--;
    score--;
    }else{
    return maxScore; // if not possible return the maaxScore
    }
    }
    return maxScore;  
    }
};