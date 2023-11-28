# Problem Link : https://leetcode.com/problems/path-sum/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def sumPath(node,total):
            if node is None:
                return False
            total+=node.val
            if node.left is None and node.right is None:
                return total == targetSum
            return (sumPath(node.left,total) or sumPath(node.right,total))
        return sumPath(root,0)
        
            
        