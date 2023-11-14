# Problem Link : https://leetcode.com/problems/shortest-word-distance/description/

class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        pos_w1 = -1
        pos_w2 = -1
        ans = float("infinity")
        for i in range(len(wordsDict)):
            if wordsDict[i]==word1:
                pos_w1=i
            if wordsDict[i]==word2:
                pos_w2 = i
            pos = pos_w1-pos_w2 if pos_w1 > pos_w2 else pos_w2-pos_w1
            if pos < ans and pos_w1!=-1 and pos_w2 != -1:
                ans = pos
        return ans