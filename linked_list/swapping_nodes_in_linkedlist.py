# Problem Link : https://leetcode.com/problems/swapping-nodes-in-a-linked-list/description/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        slow = head
        fast = head
        prev_fast = head
        for _ in range(k):
            prev_fast = fast
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next
        prev_fast.val, slow.val = slow.val, prev_fast.val
        return head


        
        