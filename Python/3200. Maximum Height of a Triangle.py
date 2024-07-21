class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        red, blu = sorted([red, blue])
        odd = even = 0
        
        for i in count(1):
            if i & 1:
                odd += i
            else:
                even += i
            a, b = sorted((odd, even))
            
            if a > red or b > blu:
                return i - 1
                