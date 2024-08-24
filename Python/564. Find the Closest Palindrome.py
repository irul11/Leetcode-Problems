class Solution:
    def nearestPalindromic(self, n: str) -> str:
        if int(n) <= 10 or (int(n[1:]) == 0 and n[0] == "1"):
            return str(int(n) - 1)

        if n == "1" + "0"*(len(n)-2) + "1":
            return str(int(n) - 2)
        
        if n == "9"*(len(n)):
            return str(int(n) + 2)

        def pal(base, isEven=True):
            if isEven:
                return base + "".join(reversed(base))
            return base + "".join(reversed(base[:-1])) 
              
        isEven = len(n) % 2 == 0
        palindromeBase = int(n[0: len(n) // 2]) if isEven else int(n[0: len(n) // 2 + 1])

        isPal = pal(str(palindromeBase), isEven) == n
        candidates = [palindromeBase - 1, palindromeBase + 1] if isPal else \
                    [palindromeBase - 1, palindromeBase, palindromeBase + 1]
        
        minn = inf

        for c in candidates:
            candidate = int(pal(str(c), isEven))
            if abs(candidate - int(n)) < minn:
                minn = abs(candidate - int(n))
                ans = str(c)
        
        return pal(ans, isEven)

