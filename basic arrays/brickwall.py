# Problem Link : https://leetcode.com/problems/brick-wall/description/

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        hmp = {0:0}
        for i in range(len(wall)):
            for j in range(1,len(wall[i])):
                wall[i][j]+=wall[i][j-1]

        for i in range(len(wall)):
            for j in range(len(wall[i])-1):
                if wall[i][j] in hmp:
                    hmp[wall[i][j]]+=1
                else:
                    hmp[wall[i][j]]=1
        max_ans, max_value = 0, 0          
        for key, value in hmp.items():
            if value > max_value:
                max_value = value
                max_ans = key
        return len(wall)-max_value
'''
Let's say we are given an input 

1 2 2 1
3 1 2
1 3 2
2 4
3 1 2
1 3 1 1

so, we will be able to penetrate through the brick wall without blockage only if starting point of width
is same at that point.
case 1 : [1,3,1,2,3,1] We will cross 3, 2, 3
case 2 : [2(from middle),3,3,2,3,3] We will cross 2,3,3,3,3
case 3 : [2(end),1(start),3,4,1,3] We will cross

1 3 5 6
3 4 6
1 4 6
2 6
3 4 6
1 4 5 6

'''