# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrderIterative(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque()
        q.append((root, 0))
        result = []

        while q:
            curr, depth = q.popleft()
            if len(result) <= depth:
                result.append([curr.val])
            else:
                result[depth].append(curr.val)
            if curr.left:
                q.append((curr.left, depth + 1))
            if curr.right:
                q.append((curr.right, depth + 1))

        return result

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        
        def dfs(node, level):
            if not node:
                return
            if len(result) == level:
                result.append([node.val])
            else:
                result[level].append(node.val)
            
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
                
        dfs(root, 0)
        return result
