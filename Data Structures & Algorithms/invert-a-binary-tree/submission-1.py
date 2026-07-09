# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root or not root.left and not root.right:
            return root

        if not root.left:
            root.left = self.invertTree(root.right)
            root.right = None
            return root

        if not root.right:
            root.right = self.invertTree(root.left)
            root.left = None
            return root

        invertedLeft = self.invertTree(root.left)
        invertedRight = self.invertTree(root.right)

        root.left = invertedRight
        root.right = invertedLeft

        return root
        