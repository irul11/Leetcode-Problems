class Solution:
    def minimumChairs(self, s: str) -> int:
        c = remains = 0
        n = len(s)
        for i in range(n):
            if s[i] == "E" and remains == 0:
                c += 1
            elif s[i] == "E":
                remains -= 1
            else:
                remains += 1
        return c
            