# Problem Link : https://leetcode.com/problems/redundant-connection/description/

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        parent = [i for i in range(len(edges)+1)]
        rank = [0]*(len(edges)+1)

        def find(n):
            p = parent[n]

            while p!=parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p
        
        def union(n1,n2):
            parent1 = find(n1)
            parent2 = find(n2)
            if parent1==parent2:
                return False
            if rank[parent1]>rank[parent2]:
                parent[parent2]=parent1
                rank[parent1]+=rank[parent2]
            else:
                parent[parent1]=parent2
                rank[parent2]+=rank[parent1]
            return True
        
        for v1, v2 in edges:
            if union(v1,v2)==False:
                return [v1,v2]
