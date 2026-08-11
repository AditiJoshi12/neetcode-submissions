# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inorder_arr = [] 

        def inorder(root: Optional[TreeNode]): 
            if root is None:
                return 

            inorder(root.left)
            inorder_arr.append(root.val)
            inorder(root.right)
            

        inorder(root)
        return inorder_arr[k-1]
