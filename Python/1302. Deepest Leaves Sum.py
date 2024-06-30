# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q = deque([(root, 0)])
        ans = 0
        curr_level = 0

        while q:
            curr, level = q.popleft()
            if level != curr_level:
                ans = 0
                curr_level = level
            ans += curr.val

            if curr.left:
                q.append((curr.left, level + 1))
            if curr.right:
                q.append((curr.right, level + 1))

        return ans
        