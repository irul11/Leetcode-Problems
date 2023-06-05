class Solution:
    def reverse(self, x: int) -> int:
        pengali = 1
        hasil = 0
        if x < 0:
            x *= -1
            pengali = -1
        for i in range(len(str(x))):
            hasil *= 10
            hasil += x % 10
            x //= 10
        return hasil * pengali if -(2 ** 31) <= hasil * pengali <= (2 ** 31) else 0
