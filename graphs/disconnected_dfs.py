from collections import defaultdict

def DFSRec(adj, s, visited):
    visited[s]=True
    print(s, end=" ")
    for u in adj[s]:
        if not visited[u]:
            DFSRec(adj,u,visited)


def DFS(adj, V):
    visited = [False]*V
    for i in range(V):
        if not visited[i]:
            DFSRec(adj, i, visited)


def addEdge(adj,u,v):
    adj[u].append(v)
    adj[v].append(u)

if __name__=="__main__":
    V = 5
    adj = defaultdict(list)
    addEdge(adj, 0, 1)
    addEdge(adj, 0, 2)
    addEdge(adj, 1, 2)
    addEdge(adj, 3, 4)
    print("Following is Depth First Traversal for disconnected graphs:")
    DFS(adj, V)