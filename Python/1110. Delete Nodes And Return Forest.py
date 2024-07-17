# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        sets = set(to_delete)

        ans = []

        def helper(root):
            if not root:
                return False
            
            if helper(root.left):
                root.left = None
            if helper(root.right):
                root.right = None
            # print(root)
            if root.val in sets:
                if root.left:
                    ans.append(root.left)
                if root.right:
                    ans.append(root.right)
            
                return True

            return False

        if not helper(root):
            ans.append(root)
            
        return ans
