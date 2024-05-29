# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif p and q:
            pass
        else:
            return False
            
        arrp = [p]
        arrq = [q]

        while arrp:
            curr_p = arrp.pop()
            curr_q = arrq.pop()

            if curr_p.val != curr_q.val:
                return False

            if curr_p.right and curr_q.right:
                arrp.append(curr_p.right)
                arrq.append(curr_q.right)
            elif not curr_p.right and not curr_q.right:
                pass
            else:
                return False

            if curr_p.left and curr_q.left:
                arrp.append(curr_p.left)
                arrq.append(curr_q.left)
            elif not curr_p.left and not curr_q.left:
                pass
            else:
                return False
        
        return True

        