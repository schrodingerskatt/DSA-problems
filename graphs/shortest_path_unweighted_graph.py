'''
Given an Unweighted Graph and a source point, the task is to find the shortest path between the source 
point and every other point in the graph.
'''

from collections import deque

def BFS(adj, V, s):
    visited = [False] * V
    dist = [0] * V
    visited[s] = True
    queue = deque()
    queue.append(s)

    while queue:
        u = queue.popleft()

        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                dist[v] = dist[u] + 1
                queue.append(v)

    print(dist)

def add_edge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)

def main():
    V = 4
    adj = [[] for _ in range(V)]
    add_edge(adj, 0, 1)
    add_edge(adj, 1, 2)
    add_edge(adj, 2, 3)
    add_edge(adj, 0, 2)
    add_edge(adj, 1, 3)
    BFS(adj, V, 0)

if __name__ == "__main__":
    main()
