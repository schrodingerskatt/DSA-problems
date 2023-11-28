# Problem Link : https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque()
        res = []
        q.append(root)
        while q:
            levels = []
            qlen = len(q)
            for i in range (qlen):
                node = q.popleft()
                if node:
                    q.append(node.left)
                    q.append(node.right)
                    levels.append(node.val)
            if levels:
                res.append(levels)
        return res
            
        