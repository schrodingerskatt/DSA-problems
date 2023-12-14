from collections import defaultdict

def DFSRec(adj, s, visited):
    visited[s]=True
    print(s, end="")

    for u in adj[s]:
        if not visited[u]:
            DFSRec(adj, u, visited)

def DFS(adj, V, s):
    visited=[False]*V
    DFSRec(adj, s, visited)

def addEdge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)

if __name__=="__main__":
    V = 5
    adj = defaultdict(list)

    addEdge(adj, 0, 1)
    addEdge(adj, 0, 2)
    addEdge(adj, 2, 3)
    addEdge(adj, 1, 3)
    addEdge(adj, 1, 4)
    addEdge(adj, 3, 4)
    print("Following is Depth First Traversal:")
    DFS(adj, V, 0)

'''
Applications of DFS:

1. Cycle Detection
2. Topological Sorting
3. Strongly Disconnected Components
4. Solving Maze and Similar Puzzles
5. Path Finding 
'''