# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(path, node):
            path ^= 1 << node.val

            nonlocal res
            #  path & (path - 1) checking if path has maximum one value odd
            if not node.left and not node.right and path & (path - 1) == 0:
                print(bin(path), bin(path-1))
                res += 1
            
            if node.left:
                dfs(path, node.left)
            if node.right:
                dfs(path, node.right)

        dfs(0, root)
        return res
            