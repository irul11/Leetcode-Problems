class Solution:
    def minOperations(self, s: str) -> int:
        result = [0, 0]
        left = ["0", "1"]
        right = ["1", "0"]

        for i in range(0, len(s)):
            if s[i] != left[i % 2]:
                result[0] += 1
            if s[i] != right[i % 2]:
                result[1] += 1

        return min(result)
