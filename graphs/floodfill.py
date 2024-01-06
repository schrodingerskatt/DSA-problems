# Problem Link : https://leetcode.com/problems/flood-fill/description/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        if image[sr][sc]==color:
            return image
        pixel = image[sr][sc]
        n = len(image)
        m = len(image[0])
        visited = [[False for _ in range (m)]for _ in range(n)]

        def DFS(i,j):
            if i < 0 or j < 0 or i >= n or j >=m or visited[i][j]==True or image[i][j]!=pixel:
                return 
            visited[i][j]=True
            image[i][j]=color
            DFS(i+1,j)
            DFS(i,j+1)
            DFS(i-1,j)
            DFS(i,j-1)

        DFS(sr,sc)
        return image