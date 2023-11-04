# Problem Link : https://leetcode.com/problems/linked-list-cycle-ii/description/
# Explaination : https://www.educative.io/answers/why-does-floyds-cycle-detection-algorithm-work

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hare = head
        tortoise = head
        while hare and hare.next:
            hare = hare.next.next
            tortoise = tortoise.next
            if hare == tortoise:
                hare = head
                while hare != tortoise:
                    hare = hare.next
                    tortoise = tortoise.next
                return hare
        return None

        