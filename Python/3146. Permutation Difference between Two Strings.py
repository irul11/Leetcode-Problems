class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        result = 0
        dict_t, dict_s = dict(), dict()
        for i in range(len(s)):
            dict_t[t[i]] = i
            dict_s[s[i]] = i
        for j in dict_s:
            result += abs(dict_t[j]-dict_s[j])
        return result
                