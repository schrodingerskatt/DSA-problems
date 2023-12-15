# Problem Link : https://leetcode.com/problems/clone-graph/description/

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        copy_dict={}
        def dfs(node):
            if node in copy_dict:
                return copy_dict[node]
            copy = Node(node.val)
            copy_dict[node]=copy
            for nbh in node.neighbors:
                copy.neighbors.append(dfs(nbh))
            return copy 
        return dfs(node) if node else None
        