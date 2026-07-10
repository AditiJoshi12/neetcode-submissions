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
        hRight = self.height(root.right)

        if hLeft != -1 and hRight != -1 and abs(hLeft - hRight) <= 1:
            return 1 + max(hLeft, hRight)
        else:
            return -1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        hLeft = self.height(root.left)
        hRight = self.height(root.right)

        if hLeft != -1 and hRight != -1 and abs(hLeft-hRight) <= 1:
            return True
        else:
            return False
            