'''
This problem discusses the Detection of a Cycle in an Undirected Graph.
'''

from collections import defaultdict

def DFSCycle(adj, s, visited, parent):
    visited[s] = True
    for u in adj[s]:
        if not visited[u]:
            if DFSCycle(adj, u, visited, s):
                return True
        elif u != parent:
            return True
    return False

def DFS(adj, V):
    visited = [False] * V
    parent = -1
    for i in range(V):
        if not visited[i]:
            if DFSCycle(adj, i, visited, parent):
                print("Cycle detected")
                return
    print("No Cycle in the Graph")

def addEdge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)

def main():
    V = 6
    adj = defaultdict(list)
    addEdge(adj, 0, 1)
    addEdge(adj, 1, 2)
    addEdge(adj, 2, 4)
    addEdge(adj, 4, 5)
    addEdge(adj, 1, 3)
    addEdge(adj, 2, 3)
    DFS(adj, V)

if __name__ == "__main__":
    main()
