class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_index = {value: i for i, value in enumerate(inorder)}
        pre_index = 0

        def build(lo, hi):
            nonlocal pre_index

            if lo > hi:
                return None

            value = preorder[pre_index]
            pre_index += 1

            root = TreeNode(value)
            split = inorder_index[value]

            root.left = build(lo, split - 1)
            root.right = build(split + 1, hi)
            return root

        return build(0, len(inorder) - 1)