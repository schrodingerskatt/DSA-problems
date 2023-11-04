# Problem link : https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

      small_node = ListNode(0)
      big_node = ListNode(0)

      small = small_node
      big = big_node

      start = head

      while start:
          if start.val < x:
              small.next = start
              small = small.next
          else:
              big.next = start
              big = big.next
          start = start.next

      small.next = big_node.next
      big.next = None

      return small_node.next
          

          

        