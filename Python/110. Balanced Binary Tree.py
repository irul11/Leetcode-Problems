# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    balance = True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])

        def dfs(node, level):
            if not node:
                return level - 1

            left = dfs(node.left, level + 1)
            right = dfs(node.right, level + 1)
            
            if abs(left-right) > 1:
                self.balance = False
            
            return max(left, right)
        
        dfs(root, 1)
        return self.balance
        