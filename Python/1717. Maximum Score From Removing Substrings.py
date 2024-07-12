class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x < y:
            s = s[::-1]
            x, y = y, x
        
        ac = bc = total = 0

        for i in range(len(s)):
            if s[i] == "a":
                ac += 1
            elif s[i] == "b":
                if ac > 0:
                    ac -= 1
                    total += x
                else:
                    bc += 1
            else:
                total += min(bc, ac) * y
                ac = bc = 0
        
        total += min(bc, ac) * y

        return total
