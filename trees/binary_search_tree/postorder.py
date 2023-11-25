# Problem Link : https://leetcode.com/problems/binary-tree-postorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def postorder(node):
            if node:
                postorder(node.left)
                postorder(node.right)
                res.append(node.val)
        postorder(root)
        return res

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        st1 = [root]
        st2 = []

        while st1:
            curr = st1.pop()
            st2.append(curr.val)
            if curr.left!=None:
                st1.append(curr.left)
            if curr.right!=None:
                st1.append(curr.right)
        return st2[::-1]