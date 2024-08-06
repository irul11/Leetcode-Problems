class Solution:
    def minimumPushes(self, word: str) -> int:
        counter = list(Counter(word).values())
        keyCounter = i = 1
        ans = 0
        counter.sort(reverse=True)
        
        for c in counter:
            ans += i * c
            keyCounter += 1
            if keyCounter == 9:
                keyCounter = 1
                i += 1

        return ans
