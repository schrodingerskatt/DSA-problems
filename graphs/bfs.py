from collections import deque

def BFS(adj, V, s):
    visited = [False]*V
    queue =deque()

    visited[s]=True
    queue.append(s)

    while queue:
        u = queue.popleft()
        print(u, end="")

        for v in adj[u]:
            if not visited[v]:
                visited[v]=True
                queue.append(v)
def add_edge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)

def main():
    V = 5
    adj = [[] for _ in range(V)]
    add_edge(adj, 0, 1)
    add_edge(adj, 0, 2)
    add_edge(adj, 1, 2)
    add_edge(adj, 2, 3)
    add_edge(adj, 1, 3)
    add_edge(adj, 3, 4)
    add_edge(adj, 2, 4)

    print("Following is Breadth First Traversal:")
    BFS(adj, V, 0)

if __name__ == "__main__":
    main()


'''
Applications of BFS:

1. Shortest path in an unweighted graph.
2. Crawlers in Search Engine.
3. Peer to Peer Network.
4. Social Networking Search.
5. Cycle Detection.
6. In Garbage Collection.
7. Ford Fulkerson Algorithm.
8. Broadcasting
'''