# Problem Link : https://leetcode.com/problems/range-sum-of-bst/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        sum = 0
        def inorder(node):
            nonlocal sum
            if node:
                inorder(node.left)
                if node.val >= low and node.val <= high:
                    sum+=node.val
                inorder(node.right)
        inorder(root)
        return sum

        