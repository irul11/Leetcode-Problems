class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        counterRow = [(0, 0)] * n
        ans = 0

        for row in grid:
            rowx = rowy = 0
            for j, s in enumerate(row):
                x, y = counterRow[j]
                if s == "X":
                    x += 1
                elif s == "Y":
                    y += 1
                
                counterRow[j] = (x, y)
                rowx += x
                rowy += y

                if rowx > 0 and rowx == rowy:
                    ans += 1
            # print(rowx, rowy, counterRow)

        return ans
