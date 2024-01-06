# Problem Link : https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/description/

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        count = 0

        def dfs(adj,node,parent):
            nonlocal count
            for child, sign in adj[node]:
                if child != parent:
                    count+=sign
                    dfs(adj,child,node)


        adj = [[] for _ in range(n)]
        for c in connections:
            adj[c[0]].append((c[1],1))
            adj[c[1]].append((c[0],0))
        dfs(adj,0,-1)
        return count

'''
1. City 'O' can only be visited, if there is path from all cities to zero. 
2. The edge should be directed from child to parent instead of parent to child, then only all child nodes
    will be able to visit their parent.
3. hence, we need to count only those edges which are from child to parent, because these nodes are
   supposed to be reversed.
4. since, there is only one way to travel between two different cities, to visit all nodes, we need to 
   first convert this given graph to bi-directional.

'''