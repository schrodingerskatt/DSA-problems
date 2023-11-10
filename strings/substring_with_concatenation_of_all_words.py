# Problem Link : https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        result = []
        hmp = {}
        for word in words:
            if word in hmp:
                hmp[word]+=1
            else:
                hmp[word]=1
        
        j = (len(words[0])*len(words))-1
        i = 0

        while j < len(s):
            a = i
            b = i+len(words[0])-1
            tmp = {}
            while b <= j:
                if s[a:b+1] in tmp:
                    tmp[s[a:b+1]]+=1
                else:
                    tmp[s[a:b+1]]=1
                a=b+1
                b+=len(words[0])
            if tmp == hmp:
                result.append(i)
            i+=1
            j+=1
        return result

        


        