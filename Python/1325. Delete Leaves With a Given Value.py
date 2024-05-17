# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def dfs(root):
            if root.left and dfs(root.left):
                root.left = None
            if root.right and dfs(root.right):
                root.right = None
                
            if not root.left and not root.right:
                if root.val == target:
                    return True
                else:
                    return False
            return False

        if dfs(root):
            return None
        else:
            return root
