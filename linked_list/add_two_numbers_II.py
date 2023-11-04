# problem link : https://leetcode.com/problems/add-two-numbers-ii/description/

# reversal approach

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverse(self, head):
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        l1 = self.reverse(l1)
        l2 = self.reverse(l2)

        carry = 0
        dummy = ListNode()
        start = dummy
        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            sum = x + y + carry
            carry = sum // 10
            digit = sum % 10
            new_node = ListNode(digit)
            start.next = new_node
            start = start.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        result = self.reverse(dummy.next)
        return result
        
# stack approach

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    stack1, stack2 = [], []
    
    while l1:
        stack1.append(l1.val)
        l1 = l1.next
    while l2:
        stack2.append(l2.val)
        l2 = l2.next

    carry = 0
    dummy = ListNode(0)
    
    while stack1 or stack2 or carry:
        x = stack1.pop() if stack1 else 0
        y = stack2.pop() if stack2 else 0
        total = x + y + carry
        carry = total // 10
        digit = total % 10
        
        new_node = ListNode(digit)
        new_node.next = dummy.next
        dummy.next = new_node
    
    return dummy.next

            
        