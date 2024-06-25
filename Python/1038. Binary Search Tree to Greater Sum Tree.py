# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:

        def helper(root, total=0):
            if not root:
                return total
            right = helper(root.right, total)
            root.val += right
            left = helper(root.left, root.val)

            return left
        
        helper(root)
        
        return root
    