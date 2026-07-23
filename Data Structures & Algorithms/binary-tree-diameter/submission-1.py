# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.max_dia = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def height(root: Optional[TreeNode]) -> int:
            if not root:
                return 0

            lHeight = height(root.left)
            rHeight = height(root.right)

            self.max_dia = max(self.max_dia, lHeight + rHeight)

            return 1 + max(height(root.left), height(root.right))

        height(root)

        return self.max_dia
        