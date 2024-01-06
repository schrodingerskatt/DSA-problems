# Problem Link : https://www.thejoboverflow.com/p/p1913/

from collections import defaultdict
n = int(input())
words = []
for i in range(n):
    ele = input()
    words.append(ele)

q = int(input())
queries = []
for i in range(q):
    ele = input()
    queries.append(ele)

set_words = set()
queries_words = set()

hmp = defaultdict()
for i in range(n):
    sorted_str = ''.join(sorted(words[i]))
    if sorted_str in hmp:
        hmp[sorted_str].append(words[i])
    else:
        hmp[sorted_str] = [words[i]]
ans = []
for qe in queries:
    s = ''.join(sorted(qe))
    if s in hmp:
        ans.append(hmp[s])
print(ans)





