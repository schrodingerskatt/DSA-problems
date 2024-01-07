# Problem Link : https://leetcode.com/problems/reaching-points/description/

sx = int(input())
sy = int(input())
tx = int(input())
ty = int(input())

while (tx > sx and ty > sy):
    if tx > ty:
        tx = tx%ty
    else:
        ty = ty%tx
flag = False
if (sx == tx and ty >= sy):
    flag = (ty-sy)%tx == 0
elif (sy == ty and tx >= sx):
    flag = (tx-sx)%ty == 0
print(flag)