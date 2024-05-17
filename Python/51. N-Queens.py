class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        result = []
        arr = [["."] * (n) for _ in range(n)]
        cols, negative_diags, positive_diags = set(), set(), set()
        
        def dfs(y):
            if y == n:
                result.append([a for a in arr])
                print(arr)
                return 
            
            for x in range(n):
                if self.isValid(x, y, cols, negative_diags, positive_diags):
                    arr[x][y] = "Q"
                    cols.add(x)
                    negative_diags.add(x-y)
                    positive_diags.add(x+y)

                    dfs(y+1)
                    
                    arr[x][y] = "."
                    cols.remove(x)
                    negative_diags.remove(x-y)
                    positive_diags.remove(x+y)
            
            return 
        
        dfs(0)
        return result
    
    def isValid(self, x, y, cols, negative_diags, positive_diags):
        if x in cols or (x-y) in negative_diags or (x+y) in positive_diags:
            return False
        return True
    