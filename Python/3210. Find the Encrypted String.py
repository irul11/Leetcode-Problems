class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        # ans = ""
        # for i in range(len(s)):
        #     ans += s[(i+k) % len(s)]
        # return ans
        return s[k%len(s):] + s[:k%len(s)]
    