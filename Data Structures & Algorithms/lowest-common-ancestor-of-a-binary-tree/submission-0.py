# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':        
        def find_path(node, target):
            if not node:
                return []
            
            if node == target:
                return [node]
            else:
                left_result = find_path(node.left, target)
                if left_result:
                    return [node] + left_result
                right_result = find_path(node.right, target)
                if right_result:
                    return [node] + right_result
                return []
        
        p_path = find_path(root, p)
        q_path = find_path(root, q)

        print([node.val for node in p_path], [node.val for node in q_path])
        i = 0
        result = None
        while i < len(p_path) and i < len(q_path) and p_path[i] == q_path[i]:
            result = p_path[i]
            i += 1
        
        return result
            
        