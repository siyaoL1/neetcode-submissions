# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = [(root, (-float("inf"), float("inf") ))]

        while stack:
            curr, boundary = stack.pop()
            # print(curr.val, boundary)
            if curr.left:
                if curr.val <= curr.left.val or curr.left.val <= boundary[0]:
                    return False
                stack.append((curr.left, (boundary[0], curr.val)))

            if curr.right:
                if curr.val >= curr.right.val or curr.right.val >= boundary[1]:
                    return False
                stack.append((curr.right, (curr.val, boundary[1]))) 
            
        return True
