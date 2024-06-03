class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        left =0

        for i in range(len(s)):
            if s[i] == t[left]:
                left += 1
            if left >= len(t):
                return 0

        return len(t) - left
