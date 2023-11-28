# Problem Link : https://leetcode.com/problems/count-complete-tree-nodes/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:


    def leftnode(self,root):
        if not root:
            return 0
        temp = root
        lh = 0
        while temp:
            temp = temp.left
            lh+=1
        return lh
    def rightnode(self,root):
        if not root:
            return 0
        temp = root
        rh = 0
        while temp:
            temp = temp.right
            rh+=1
        return rh
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        lh = self.leftnode(root)
        rh = self.rightnode(root)
        if lh == rh:
            return (2**lh)-1
        return 1+self.countNodes(root.left)+self.countNodes(root.right)