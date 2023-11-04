# Problem link : https://leetcode.com/problems/copy-list-with-random-pointer/description/

# Space Complexity : O(n) Approach

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        OldCopy = {None : None}
        cur = head
        while cur:
            cpy = Node(cur.val)
            OldCopy[cur] = cpy
            cur = cur.next
        
        cur = head
        while cur:
            cpy = OldCopy[cur]
            cpy.next = OldCopy[cur.next]
            cpy.random = OldCopy[cur.random]
            cur = cur.next
        return OldCopy[head]
        
# Space Complexity : O(1) Approach

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return head

      
        curr = head
        
        while curr:
            temp = curr.next
            curr.next = Node(curr.val)
            curr.next.next = temp
            curr = temp
        
        curr = head
        
        while curr:
            curr.next.random = curr.random.next if curr.random else None
            curr = curr.next.next
            
        org = head
        copy = head.next
        
        temp = copy
        
        while org:
            org.next = org.next.next
            copy.next = copy.next.next if copy.next else None
            org = org.next
            copy = copy.next
            
        return temp