class Solution:
    def numberOfChild(self, n: int, k: int) -> int:        
        direction = 1
        pos = 0
        while k > 0:
            pos += direction
            k -= 1
            
            if pos == n-1 or pos == 0:
                direction *= -1
        return pos
        