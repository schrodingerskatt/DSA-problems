'''
Topological Sort using Kahn's BFS

1. Store indegree of every vertex.
2. Create a queue.
3. Add all 0 indegree vertices to the queue.
4. while(queue is not empty)
   a. u = queue.pop()
   b. print(u)
   c. for every adjacent v of u
      c.1. reduce indegree of v by 1
      c.2. if indegree of v becomes 0, add v to the queue
'''
from collections import deque, defaultdict

def topologicalSort(adj, V):

    indegree = [0]*V

    for u in range(V):
        for x in adj[u]:
            indegree[x]+=1
    
    q = deque()
    for u in range(V):
        if indegree[u]==0:
            q.append(u)
    
    while q:
        v = q.popleft()
        print(v, end=" ")

        for x in adj[v]:
            indegree[x]-=1
            if indegree[x]==0:
                q.append(x)

def addEdge(adj, u, v):
    adj[u].append(v)

if __name__=="__main__":
    V = 5
    adj = defaultdict(list)
    addEdge(adj, 0, 2)
    addEdge(adj, 0, 3)
    addEdge(adj, 1, 3)
    addEdge(adj, 1, 4)
    addEdge(adj, 2, 3)
    print("Following is a Topological Sort of")
    topologicalSort(adj, V)