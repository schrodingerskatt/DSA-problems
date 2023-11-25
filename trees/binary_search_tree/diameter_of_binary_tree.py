# Problem Link : https://leetcode.com/problems/diameter-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def height(n):
            if n is None:
                return 0
            else:
                return max(height(n.left),height(n.right))+1

        def diameter(node):
            if node is None:
                return 0
            d1 = height(node.left)+height(node.right)
            d2 = diameter(node.left)
            d3 = diameter(node.right)
            return max(d1,max(d2,d3))
        return diameter(root)
        
# Efficient Approach

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
      
        diam = 0
        def diameter(node):
            nonlocal diam
            if node is None:
                return 0
            leftn = diameter(node.left)
            rightn = diameter(node.right)
            diam = max(diam,leftn+rightn)
            return 1+max(leftn,rightn)
        diameter(root)
        return diam