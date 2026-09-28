# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        nodes = [(root, 1)]
        max_depth = 0
        while len(nodes) > 0:
            curr, depth = nodes.pop()
            max_depth = max(depth, max_depth)
            if curr.left:
                nodes.append((curr.left, depth + 1))
            if curr.right:
                nodes.append((curr.right, depth + 1))
            
        return max_depth