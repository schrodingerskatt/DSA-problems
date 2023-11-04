# Problem Link : https://leetcode.com/problems/rotate-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # length of a linked list
        if head is None or head.next is None or k == 0:
            return head

        len = 1
        temp = head
        last = head
        while last.next:
            last = last.next
            len +=1
        k = k%len
        if k == 0:
            return head
        temp = head
        for _ in range(len-k-1):
            temp = temp.next
        start = temp.next
        temp.next = None
        last.next = head
        return start