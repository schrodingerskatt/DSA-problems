# Problem Link : https://www.geeksforgeeks.org/convert-the-ascii-value-sentence-to-its-equivalent-string/

ascii_string = input()
length = len(ascii_string)

num = 0
ans =""
for i in range(length):
    digit = ord(ascii_string[i])-ord('0')
    num = num*10+digit
    if 32 <= num <= 122:
        ans+=chr(num)
        num = 0
print(ans)