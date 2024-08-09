class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if m < 3 or n < 3:
            return 0
            
        ans = 0

        for i in range(1, m-1):
            for j in range(1, n-1):
                ans += self.checking(grid, i, j)

        return ans    
    
    def checking(self, arr, i, j):
        sets = set()
        sums = [-1, -1]
        for k in range(-1, 2):
            temp = [0, 0]
            for l in range(-1, 2):
                if arr[i+k][j+l] <= 0 or arr[i+k][j+l] > 9 or arr[i+k][j+l] in sets:
                    return 0
                temp[0] += arr[i+k][j+l]
                temp[1] += arr[i+l][j+k]
                sets.add(arr[i+k][j+l])

            if sums[0] != -1 and (sums[0] != temp[0] or sums[1] != temp[1]):
                return 0
            sums = temp

        if arr[i-1][j-1] + arr[i+1][j+1] != arr[i-1][j+1] + arr[i+1][j-1]:
            return 0

        return 1
