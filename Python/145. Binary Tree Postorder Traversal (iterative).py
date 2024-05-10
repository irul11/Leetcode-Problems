# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        curr = root
        prev = [root]

        while curr:
            if curr.left:
                curr = curr.left
                prev.append(curr)
            elif curr.right:
                curr = curr.right
                prev.append(curr)
            else:
                result.append(prev.pop().val)
                if prev:
                    curr = prev[-1]
                    if curr.left:
                        curr.left = None
                    elif curr.right:
                        curr.right = None
                else:
                    curr = None

        return result
            