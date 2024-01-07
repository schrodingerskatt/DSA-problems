s = input()  
n = len(s)   
s = list(s)  
ans = ""     
i = 0
while i < n- 1:
    count = 1
    while (i < n - 1 and s[i] == s[i + 1]):
        count += 1
        i += 1
    i += 1
    print(s[i - 1] +str(count), end = "")
