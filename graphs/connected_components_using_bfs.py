'''
Find connected components in a graph using BFS
'''
from collections import deque

def BFS(adj, s, visited):
    visited[s]=True
    queue = deque()
    queue.append(s)
    while queue:
        u = queue.popleft()
        # print(u, end="")
        for v in adj[u]:
            if not visited[v]:
                visited[v]=True
                queue.append(v)


def BFS_connected(adj, V):
    visited = [False]*V
    count = 0
    for i in range(V):
        if visited[i]==False:
            BFS(adj,i,visited)
            count+=1
    return count

def add_edge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)

def main():
    V = 7
    adj = [[] for _ in range(V)]
    add_edge(adj, 0, 1)
    add_edge(adj, 0, 2)
    add_edge(adj, 2, 3)
    add_edge(adj, 1, 3)
    add_edge(adj, 4, 5)
    add_edge(adj, 5, 6)
    add_edge(adj, 4, 6)
    print(BFS_connected(adj, V))


if __name__ == "__main__":
    main()
