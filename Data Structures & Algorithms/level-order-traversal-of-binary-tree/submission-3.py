# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrderStack(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        stack = [(root, 0)]

        result = []
        while stack:
            curr, level = stack.pop()
            if curr:
                stack.append((curr.right, level + 1))
                stack.append((curr.left, level + 1))
                if level >= len(result):
                    result.append([curr.val])
                else:
                    result[level].append(curr.val)
        
        return result
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque()
        q.append((root, 0))
        result = []
        while q:
            curr, level = q.popleft()
            if curr:
                q.append((curr.left, level + 1))
                q.append((curr.right, level + 1))
                if level >= len(result):
                    result.append([curr.val])
                else:
                    result[level].append(curr.val)

        return result