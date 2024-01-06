# Heap module in python

import heapq # By default it's a min. heap

heap = []
heapq.heappush(heap, 10)
heapq.heappush(heap, 1)
heapq.heappush(heap, 5)
print(heap)

'''
heapq.heappop(heap) : will return the smallest value and also it will delete that from heap, maintaining
                      the heap property.
'''
heapq.heappop(heap)
print(heap)
'''
heapq.heapify(heap) : this function will convert a list to binary heap in place.
'''
list_h = [1,3,5,2,4,6]
heapq.heapify(list_h)
print(list_h)

'''
heapq.heappushpop(heap, item) : insert the mentioned item in the heap, maintaining the heap property.
                                will return the smallest value from the heap and delete it.
'''
heapq.heappushpop(list_h,89)
print(list_h)

'''
heapq.heapreplace(heap, item) : pop the smallest element and will insert the new element.
                                pop followed by a push.
'''
heapq.heapreplace(list_h,111)
print(list_h)

''' N smallest element number in a given iterable'''

heap = [1,20,5,4,3,6,2]
print(heapq.nsmallest(2, heap))
print(heapq.nlargest(2,heap))

# Implementing priority queue using heapq module
# [(priority, element),(...,...)]
pq = [(1,"ria"),(4,"sia"),(3,"gia")]
heapq.heapify(pq)
for i in range(len(pq)):
    print(heapq.heappop(pq))

listForTree = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]    
heapq.heapify(listForTree)
print(listForTree)             # for a min heap
print(heapq.heappop(listForTree))     # pop from minheap
heapq._heapify_max(listForTree)
print(listForTree)             # for a maxheaps
print(heapq._heappop_max(listForTree)) # pop from maxheap