class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, path_max):
            if node is None:
                return 0

            is_good = node.val >= path_max
            path_max = max(path_max, node.val)

            return (
                is_good
                + dfs(node.left, path_max)
                + dfs(node.right, path_max)
            )

        return dfs(root, float("-inf"))