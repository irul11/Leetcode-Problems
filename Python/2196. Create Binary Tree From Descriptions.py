# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        maps = dict()
        sets = set()
        for d in descriptions:
            sets.add(d[1])
            if d[0] not in maps:
                maps[d[0]] = TreeNode(d[0])
            if d[1] not in maps:
                maps[d[1]] = TreeNode(d[1])
            if d[2] == 1:
                maps[d[0]].left = maps[d[1]]
            elif d[2] == 0:
                maps[d[0]].right = maps[d[1]]

        for d in descriptions:
            if d[0] not in sets:
                return maps[d[0]]
