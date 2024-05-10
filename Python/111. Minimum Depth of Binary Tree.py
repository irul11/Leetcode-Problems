from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        arr = deque([(root, 1)])
        while arr:
            curr, level = arr.popleft()
            if not curr.left and not curr.right:
                return level
            level += 1
            if curr.left:
                arr.append((curr.left, level))
            if curr.right:
                arr.append((curr.right, level))
        

        