import heapq
k = 3
arr = [2, 6, 3, 12, 56, 8]
pq = arr[:k+1]
n = len(arr)
heapq.heapify(pq)
index = 0
for i in range(k+1,n):
    arr[index]=heapq.heappop(pq)
    heapq.heappush(pq,arr[i])
    index+=1

while pq:
    arr[index]=heapq.heappop(pq)
    index+=1

print(arr)
# : O(n+k log k)