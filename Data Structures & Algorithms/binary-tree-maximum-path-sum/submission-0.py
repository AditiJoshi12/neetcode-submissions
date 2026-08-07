# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.best = float("-inf")

        def helper(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0

            pathL = max(0, helper(root.left))
            pathR = max(0, helper(root.right))

            self.best = max(self.best, root.val + pathL + pathR)

            return root.val + max(pathL, pathR) 

        helper(root)

        return self.best
        