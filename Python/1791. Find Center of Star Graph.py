class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        sets = set(edges[0])

        if edges[1][0] in sets:
            return edges[1][0]
        elif edges[1][1] in sets:
            return edges[1][1]
            