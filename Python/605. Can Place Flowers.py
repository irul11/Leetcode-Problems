class Solution:
    def canPlaceFlowers(self, f: List[int], n: int) -> bool:
        if n == 0:
            return True

        for i in range(len(f)):
            if (f[i] == 0 and (i == 0 or f[i-1] == 0)) and (i == len(f) - 1 or f[i+1] == 0):
                f[i] = 1
                n -= 1
                if n == 0:
                    return True
        
        return False
        