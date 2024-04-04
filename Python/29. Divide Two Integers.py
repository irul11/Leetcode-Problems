class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if (dividend == -2147483648 and divisor == -1):
            return 2147483647

        a, b, result = abs(dividend), abs(divisor), 0

        for i in range(32)[::-1]:
            if (a >> i) >= b:
                result += 1 << i
                a -= b << i
        
        return result if (dividend >= 0) == (divisor >= 0) else -result