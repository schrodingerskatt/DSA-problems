# Problem Link : https://leetcode.com/problems/swap-nodes-in-pairs/description/

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while head and head.next:
            first = head
            second = head.next

            # Perform the swap
            prev.next = second
            first.next = second.next
            second.next = first

            prev = first
            head = first.next

        return dummy.next
