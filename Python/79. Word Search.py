from collections import defaultdict

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        if len(word) > m * n:
            return False

        count = defaultdict(int)
        for row in board:
            for cell in row:
                count[cell] += 1
                
        # Reverse word for simplicity next loop
        if count[word[0]] > count[word[-1]]: 
            word = word[::-1]
        for cell in word:
            if count[cell] == 0: return False
            count[cell] -= 1
        
        def backtracks(i, j, k, sets):
            if k == len(word):
                return True
            if not (0 <= i < m) or not (0 <= j < n) or (i, j) in sets or board[i][j] != word[k]:
                return False
            
            sets.add((i, j))
            result = (
                backtracks(i-1, j, k + 1, sets) or
                backtracks(i+1, j, k + 1, sets) or
                backtracks(i, j+1, k + 1, sets) or
                backtracks(i, j-1, k + 1, sets)
            )            
            sets.remove((i,j))
            return result

        sets = set()
        for i in range(m):
            for j in range(n):
                if backtracks(i,j,0,sets):
                    return True

        return False
    