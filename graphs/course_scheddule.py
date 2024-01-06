# Problem Link : https://leetcode.com/problems/course-schedule/description/

'''
In this problem we have to detect whether a cycle exist in a directed graph or not. If it exists return 
False else True. I have solved this problem using both BFS and DFS.
'''
# 1. BFS

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        indegree = [0]*numCourses
        adj = [[] for _ in range(numCourses)]

        for nodes in prerequisites:
            adj[nodes[1]].append(nodes[0])
            indegree[nodes[0]]+=1

        count = 0
        q = deque()
        for u in range(numCourses):
            if indegree[u]==0:
                q.append(u)
        
        while q:
            u = q.popleft()
            count+=1
            for v in adj[u]:
                indegree[v]-=1
                if indegree[v]==0:
                    q.append(v)
        return count==numCourses
    
# 2. DFS

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        visited = [False]*numCourses
        recvisited = [False]*numCourses
        adj = [[] for _ in range(numCourses)]

        def DFS(i):
            nonlocal visited, recvisited, adj
            visited[i]=True
            recvisited[i]=True
            for j in adj[i]:
                if not visited[j] and DFS(j):
                    return True
                if recvisited[j]==True:
                    return True
            recvisited[i]=False
            return False

        for nodes in prerequisites:
            adj[nodes[1]].append(nodes[0])
        
        for i in range(numCourses):
            if not visited[i]:
                if DFS(i):
                    return False
        return True