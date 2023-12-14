from collections import defaultdict

def DFS(adj, s, visited):
    visited[s]=True
    #print(s, end=" ")
    for u in adj[s]:
        if not visited[u]:
            DFS(adj,u,visited)


def DFS_connected(adj, V):
    visited = [False]*V
    count = 0
    for i in range(V):
        if not visited[i]:
            DFS(adj, i, visited)
            count+=1
    return count


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
    print(DFS_connected(adj, V))