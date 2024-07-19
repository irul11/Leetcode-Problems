class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        maxCols, minRows = [-1] * n, set()

        for i in range(m):
            minRow = inf
            for j in range(n):
                maxCols[j] = max(maxCols[j], matrix[i][j])
                minRow = min(minRow, matrix[i][j])
            minRows.add(minRow)

        for m in maxCols:
            if m in minRows:
                return [m]

        return []
    