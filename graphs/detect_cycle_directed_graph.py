from collections import defaultdict

def DFSrec(adj, u, visited, recvisited):
    visited[u]=True
    recvisited[u]=True
    for v in adj[u]:
        if not visited[v] and DFSrec(adj, v, visited, recvisited):
            return True
        elif recvisited[v]:
            return True
    recvisited[u] = False
    return False

def DFS(adj, V):
    visited = [False]*V
    recvisited = [False]*V
    for i in range(V):
        if not visited[i]:
            if DFSrec(adj, i, visited, recvisited):
                return True
    return False

def addEdge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)

if __name__ == "__main__":
    V = 6
    adj = defaultdict(list)
    addEdge(adj, 0, 1)
    addEdge(adj, 2, 1)
    addEdge(adj, 2, 3)
    addEdge(adj, 3, 4)
    addEdge(adj, 4, 5)
    addEdge(adj, 5, 3)
    if DFS(adj, V):
        print("Cycle found")
    else:
        print("No cycle found")