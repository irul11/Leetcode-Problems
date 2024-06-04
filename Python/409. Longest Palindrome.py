class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        odd = False
        ans = len(s)

        for c in counter:
            if counter[c] % 2 != 0 and not odd:
                odd = True
            elif counter[c] % 2 != 0:
                ans -= 1

        return ans
