# Problem Link : https://leetcode.com/problems/reorder-list/description/?source=submission-noac

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseLL(self, node):
        curr = node
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
    
    def merge(self, L1, L2):

        while L2 is not None:
            nextL1 = L1.next
            L1.next = L2
            L1 = L2
            L2 = nextL1

    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head or not head.next:
            return head

        slow = head
        fast = head
        prev = slow

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        L1 = head
        L2 = self.reverseLL(slow)
        self.merge(L1, L2)
