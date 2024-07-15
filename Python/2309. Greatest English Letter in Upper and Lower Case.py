class Solution:
    def greatestLetter(self, s: str) -> str:
        ans = 0
        sets = set()
        
        for i in range(len(s)):
            ordd = ord(s[i])
            if ordd + 32 in sets:
                ans = max(ans, ordd)
            elif ordd - 32 in sets:
                ans = max(ans, ordd - 32)
            sets.add(ordd)

        return chr(ans) if ans != 0 else ""
        