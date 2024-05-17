class Solution:
    def totalNQueens(self, n: int) -> list[list[str]]:
        cols = [False] * n
        negative_diags = [False] * (2*n + 1)
        positive_diags = [False] * (2*n + 1)
        
        def dfs(y, is_first_row = False, is_odd = False):
            result = 0
            if y == n:
                return 1 
            
            i = n//2 if is_odd and is_first_row else 0
            j = i+1 if is_odd and is_first_row else n//2 if is_first_row else n
            
            for x in range(i,j):
                if self.isValid(x, y, cols, negative_diags, positive_diags):
                    cols[x] = True
                    negative_diags[x-y] = True
                    positive_diags[x+y] = True

                    result += dfs(y+1)
                    
                    cols[x] = False
                    negative_diags[x-y] = False
                    positive_diags[x+y] = False
            
            return result 
        
        result = dfs(0, True) * 2
        if n % 2:
            result += dfs(0, True, True)
        return result
    
    def isValid(self, x, y, cols, negative_diags, positive_diags):
        if cols[x] or negative_diags[x-y] or positive_diags[x+y]:
            return False
        return True
    