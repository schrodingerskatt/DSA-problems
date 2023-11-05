# problem : https://leetcode.com/problems/maximum-population-year/description/

class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        freq = {}
        for i in logs:
            for j in range(i[0],i[1]):
                if j in freq:
                    freq[j]+=1
                else:
                    freq[j]=1
        sorted_years = sorted(freq.items(), key=lambda item: (-item[1], item[0]))
        return sorted_years[0][0]
