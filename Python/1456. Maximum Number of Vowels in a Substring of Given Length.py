class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        c = 0
        vowels = list("aeiou")

        for i in range(k):
            if s[i] in vowels:
                c += 1

        ans = c
        for i in range(k, len(s)):
            if s[i-k] in vowels:
                c -= 1
            if s[i] in vowels:
                c += 1
            ans = max(ans, c)

        return ans
            