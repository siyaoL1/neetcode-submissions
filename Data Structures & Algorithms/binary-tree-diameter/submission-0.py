# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # recurrence is that diameter =  max(1 + depth(left), 1 + depth(right), depth(left) + depth(right))
        # we keep trying to find the max diameter while storing the depth 
        # lets assume the val is unique
        result = 0


        def depth(node) -> int:
            nonlocal result
            if not node:
                return 0
            left_depth = depth(node.left)
            right_depth = depth(node.right)
            result = max(left_depth + right_depth, result)
            return max(left_depth, right_depth) + 1

        
        depth(root)

        return result