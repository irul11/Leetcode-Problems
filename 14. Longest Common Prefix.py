class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        result = ''
        if strs[0] == "":
            return ""
        while i < len(strs[0]):
            item = strs[0][i]
            for s in strs:
                if i >= len(s):
                    return result
                # print(s[i])
                if s[i] != item:
                    return result
            result += item
            i += 1
        return result


