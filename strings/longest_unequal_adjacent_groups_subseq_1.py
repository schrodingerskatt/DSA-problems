# problem link : https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/

class Solution:
    def getWordsInLongestSubsequence(self, n: int, words: List[str], groups: List[int]) -> List[str]:
        ans = []
        i, j = 0, 1
        while j < n:
            if groups[i]!=groups[j]:
                if words[i] not in ans:
                    ans.append(words[i])
                if words[j] not in ans:
                    ans.append(words[j])
                i = j
                j+=1
            else:
                j+=1
        
        if ans:
            return ans
        else:
            return [words[0]]