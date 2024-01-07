# Problem Link : https://www.desiqna.in/15745/goldman-sachs-oa-sde-set-50-august-2023-project-estimates

n = int(input())
project = []
for i in range(n):
    ele = int(input())
    project.append(ele)
target = int(input())

mp = {}
for num in project:
    if num in mp:
        mp[num]+=1
    else:
        mp[num]=1
ans = 0
for key, value in mp.items():
    if target == 0 and value > 1:
        ans+=1
    elif target+key in mp:
        ans+=1
print(ans)
