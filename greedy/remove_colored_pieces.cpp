// Problem Link : https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/description/

class Solution {
public:
    bool winnerOfGame(string colors) {
        
        int n = colors.size();
        if(n < 3) return false;
        vector<bool>Alice(n,false);
        vector<bool>Bob(n,false);

        for(int i = 1; i < colors.size()-1; i++){
        if(colors[i]=='A' && colors[i-1]=='A'&& colors[i+1] == 'A')
        Alice[i] = true;
        else if (colors[i] == 'B' && colors[i-1] == 'B' && colors[i+1] == 'B')
        Bob[i] = true;
        else{
        Alice[i] = false;
        Bob[i] = false;
        }
        }
        int count_alice = 0;
        int count_bob = 0;

        for(int i = 1; i <colors.size(); i++){
        if(Alice[i])
        count_alice++;
        if(Bob[i])
        count_bob++;
        }

        if(count_alice > count_bob) return true;
        return false;

    }
};

// More Optimal Approach

class Solution {
public:
    bool winnerOfGame(string colors) {

     int alice = 0;
     int bob = 0;
     for(int i = 1; i < colors.size() -1; i++){
        
    if(colors[i] == colors[i-1] && colors[i] == colors[i+1]){
    if(colors[i] == 'A')
    alice++;
    else
    bob++;
    }
    }
    return alice > bob ? true : false;    
    }
};