# Problem Link : https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hashset = {}
        temp = head
        while temp:
            if temp.val in hashset:
                hashset[temp.val]+=1
            else:
                hashset[temp.val] = 1
            temp = temp.next
        
        dummy = ListNode()
        start = dummy
        for key, values in hashset.items():
            if values == 1:
                node = ListNode(key)
                start.next = node
                start = start.next
            else:
                continue
        return dummy.next