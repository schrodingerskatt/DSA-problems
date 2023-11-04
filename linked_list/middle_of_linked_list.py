# Problem Link : https://leetcode.com/problems/middle-of-the-linked-list/description/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        len = 0
        temp = head
        while(temp):
            temp = temp.next
            len += 1
        temp = head

        i = 0
        while i < len//2:
            temp = temp.next
            i += 1
        return temp
         