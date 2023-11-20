class Solution:
    def smallestNumber(self, pattern: str) -> str:
        
        s =""
        n = len(pattern)
        for i in range(1,n+2):
            s+=str(i)
        i,d = 0,0

        while i < len(pattern):
            if pattern[i]=='I':
                i+=1
            else:
                j = i
                while j < n and pattern[j]=='D':
                    j+=1
                s =  s[:i] + s[i:j + 1][::-1] + s[j + 1:]
                i = j+1
        return s
                