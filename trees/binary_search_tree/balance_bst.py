# Problem Link : https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def height(node):
            if node is None:
                return 0
            return 1+max(height(node.left),height(node.right))
        
        def check_balance(node):
            if node is None:
                return True
            lh = height(node.left)
            rh = height(node.right)
            return (abs(lh-rh)<=1 and check_balance(node.left) and check_balance(node.right))
        return check_balance(root)


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def check_balance(node):
            if node is None:
                return 0
            lh = check_balance(node.left)
            if lh == -1:
                return -1
            rh = check_balance(node.right)
            if rh == -1:
                return -1
            if abs(lh-rh)>1:
                return -1
            else:
                return max(lh,rh)+1
        return check_balance(root)!=-1
        
