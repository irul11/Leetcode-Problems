class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, math.floor(math.sqrt(c))
        ans = False
        
        sets = set()
        for i in range(right + 1):
            if i**2 * 2 == c or i**2 in sets:
                return True
            sets.add(c - i**2)

        return False