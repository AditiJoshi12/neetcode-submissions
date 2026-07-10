# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def height(self, root: Optional[TreeNode]):
        if not root:
            return 0

        hLeft = self.height(root.left)
        if hLeft == -1:
            return -1

        hRight = self.height(root.right)
        if hRight == -1:
            return -1

        if abs(hLeft - hRight) <= 1:
            return 1 + max(hLeft, hRight)
        
        return -1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.height(root) != -1
            