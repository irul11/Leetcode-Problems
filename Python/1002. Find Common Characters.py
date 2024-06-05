class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        n = len(words)
        counter = []
        ans = []

        for word in words:
            counter.append(Counter(word))
        
        for c in counter[0]:
            tot = counter[0][c]
            for i in range(1, n):
                if not counter[i][c]:
                    tot = 0
                    break
                elif counter[i][c] < tot:
                    tot = counter[i][c]
            ans += [c] * tot

        return ans
            
