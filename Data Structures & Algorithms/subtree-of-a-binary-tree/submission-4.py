# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def match(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            
            return (
                p.val == q.val and 
                match(p.left, q.left) and 
                match(p.right, q.right)
            )
        def search(p, q):
            if not p:
                return False
            if match(p, q):
                return True
            
            return search(p.left, q) or search(p.right, q)
        
        return search(root, subRoot)