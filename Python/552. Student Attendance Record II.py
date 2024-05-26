class Solution:
    def checkRecord(self, n: int) -> int:
        import numpy as np

        matrix = np.array([
            [1,1,0,1,0,0],
            [1,0,1,1,0,0],
            [1,0,0,1,0,0],
            [0,0,0,1,1,0],
            [0,0,0,1,0,1],
            [0,0,0,1,0,0]
        ])
        mod = 10**9 + 7

        def mat_pow(matrix, power):
            if power == 1:
                return matrix
            if power % 2 == 0:
                temp = mat_pow(matrix, power // 2)
                return (temp @ temp) % mod
            else:
                return (matrix @ mat_pow(matrix, power - 1)) % mod
        
        ans = mat_pow(matrix, n)

        return int(sum(ans[0]) % mod)
        