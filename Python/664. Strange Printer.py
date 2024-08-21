class Solution:
    def strangePrinter(self, s: str) -> int:
        def minimumTurns(start, end, s, memo):
            if start > end:
                return 0
            
            if memo[start][end] != -1:
                return memo[start][end]

            minTurns = 1 + minimumTurns(start + 1, end, s, memo)

            for k in range(start + 1, end + 1):
                if s[k] == s[start]:

                    turnsWithMatch = minimumTurns(start, k - 1, s, memo) + minimumTurns(k + 1, end, s, memo)
                    minTurns = min(minTurns, turnsWithMatch)
            
            memo[start][end] = minTurns
            return minTurns
        
        def removeDuplicates(s):
            uniq = ""
            i = 0
            while i < len(s):
                curr = s[i]
                uniq += curr
                while i < len(s) and s[i] == curr:
                    i += 1
            
            return uniq
        
        s = removeDuplicates(s)
        n = len(s)
        memo = [[-1] * (n) for _ in range(n)]

        return minimumTurns(0, n-1, s, memo)
                