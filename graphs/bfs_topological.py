'''
Topological Sort using BFS

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