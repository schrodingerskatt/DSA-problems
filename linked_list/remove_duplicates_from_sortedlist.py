# Problem Link : https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        start = head
        while start and start.next:
            if start.val == start.next.val:
                start.next = start.next.next
            else:
                start = start.next
                
        return head
        