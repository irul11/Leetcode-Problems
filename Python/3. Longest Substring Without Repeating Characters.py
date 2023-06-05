class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        result = 0
        length = 0
        left = 0
        for i, j in enumerate(s):
            if j not in dic:
                dic[j] = i
            else:
                if dic[j] >= left:
                    left = dic[j] + 1
                dic[j] = i
            length = len(s[left:i + 1])
            # print(length)
            # print(s[left:i+1])
            if length > result:
                result = length

        return result
