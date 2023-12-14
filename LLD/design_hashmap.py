# Problem Link : https://leetcode.com/problems/design-hashmap/


class ListNode:
    def __init__(self, key = -1, val = -1, next = None):
        self.key = key
        self.val = val
        self.next = None


class MyHashMap:

    def __init__(self):
        self.map = [ListNode() for i in range(10001)]

    def put(self, key: int, value: int) -> None:
        curr = self.map[key%len(self.map)]
        while curr.next:
            if curr.next.key == key:
                curr.next.val = value
                return 
            curr = curr.next
        curr.next = ListNode(key,value)


    def get(self, key: int) -> int:
        curr = self.map[key%len(self.map)].next
        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next
        return -1
        
    def remove(self, key: int) -> None:
        curr = self.map[key%len(self.map)]
        while curr and curr.next: # what if we have to remove forst node
            if curr.next.key == key:
                curr.next = curr.next.next
                return 
            curr = curr.next
        

