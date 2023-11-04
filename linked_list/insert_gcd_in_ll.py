# Problem Link : https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def GCD(self, x, y):
        while(y):
            x, y = y, x % y
        return abs(x)
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        prev = head
        curr = head.next
        
        while curr:
            gcd = self.GCD(prev.val, curr.val)
            node_val = ListNode(gcd)
            temp = prev.next
            prev.next = node_val
            node_val.next = temp
            prev = prev.next.next
            curr = curr.next
        return dummy.next

        
