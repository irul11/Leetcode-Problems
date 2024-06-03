# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        prev = [root]

        while prev:
            curr = prev.pop()
            result.append(curr.val)
            
            if curr.right:
                prev.append(curr.right)
            if curr.left:
                prev.append(curr.left)

        return result
        