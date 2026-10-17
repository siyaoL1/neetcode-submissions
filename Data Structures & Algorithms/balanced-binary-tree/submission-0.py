# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # I think this problem is pretty intuitive as a recursive solution
        # but I also want to try to think of how it'd look like in sequential scenerio
        def height(node):
            if not node:
                return (0, True)
            
            left_height, left_valid = height(node.left)
            right_height, right_valid = height(node.right)
            new_height = max(left_height, right_height) + 1

            if not left_valid or not right_valid or abs(left_height - right_height) > 1:
                return (new_height, False)
            return (new_height, True)
        
        return height(root)[1]

        