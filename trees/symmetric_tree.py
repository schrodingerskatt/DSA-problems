# Problem Link : https://leetcode.com/problems/symmetric-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        def mirror(l,r):
            if l is None and r is None:
                return True
            if l is None or r is None:
                return False
            return (l.val == r.val and mirror(l.left,r.right) and mirror(l.right, r.left))
        return mirror(root.left, root.right)
        