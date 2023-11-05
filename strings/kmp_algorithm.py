# This algorithm is pretty pain in the a$$, would advise you to take a complete day to fully understand it.
# Here, are two video links, whic helped in understanding this algorithm
# NeetCode : https://www.youtube.com/watch?v=JoF0Z7nVSrA
# LogicFirst : https://www.youtube.com/watch?v=4jY57Ehc14Y&t=1132s

def KMP(pat, txt):
    N = len(txt)
    M = len(pat)
    lps = [0] * M
    computeLPS(pat, M, lps)
    i, j = 0, 0
    while i < N:
        if txt[i] == pat[j]:
            i += 1
            j += 1
        if j == M:
            print("Pattern found at index", i - j)
            j = lps[j - 1]  # to find index of next occurring pattern in txt
        elif i < N and txt[i] != pat[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

def computeLPS(pat, M, lps):
    length = 0
    lps[0] = 0
    i = 1

    while i < M:
        if pat[i] == pat[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

if __name__ == '__main__':
    txt = "ABABDABACDABABCABAB"
    pat = "ABABCABAB"
    KMP(pat, txt)

# time complexity : O(n+m)