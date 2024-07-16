# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], sv: int, dv: int) -> str:
        ss = []
        ds = []

        def helper(root, arr, d):
            if root.val == d:
                return True
            
            if root.left and helper(root.left, arr, d):
                arr.append("L")
            elif root.right and helper(root.right, arr, d):
                arr.append("R")

            return arr

        helper(root, ss, sv)
        helper(root, ds, dv)

        while len(ss) and len(ds) and ss[-1] == ds[-1]:
            ss.pop()
            ds.pop()
            
        return ("U" * len(ss)) + "".join(reversed(ds))
