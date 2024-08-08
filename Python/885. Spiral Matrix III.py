class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rs: int, cs: int) -> List[List[int]]:
        visited = set()
        arr = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dirIdx = 3

        while len(arr) < rows * cols:
            if 0 <= rs < rows and 0 <= cs < cols:
                visited.add((rs, cs))
                arr.append([rs, cs])
            tempRow, tempCol = rs + directions[(dirIdx + 1) % 4][0], cs + directions[(dirIdx + 1) % 4][1]

            if (tempRow, tempCol) not in visited:
                dirIdx = (dirIdx + 1) % 4
                rs = tempRow
                cs = tempCol
            else:
                rs += directions[dirIdx][0]
                cs += directions[dirIdx][1]
    
        return arr
    