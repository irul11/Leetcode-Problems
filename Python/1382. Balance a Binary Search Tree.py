# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr = []

        def helper(root, arr):
            if not root:
                return
            
            helper(root.left, arr)
            arr.append(root.val)
            helper(root.right, arr)

        def generate(arr):
            if not arr:
                return 
            mid = len(arr)//2

            newRoot = TreeNode()
            newRoot.val = arr[mid]
            newRoot.left = generate(arr[:mid])
            newRoot.right = generate(arr[mid+1:])
            
            return newRoot
        
        helper(root, arr) 
        root = None
        # print(newRoot)
        return generate(arr)