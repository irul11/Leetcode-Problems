from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        dicts = defaultdict(list)
        for str in strs:
            sorted_str = "".join(sorted(str))
            dicts[sorted_str].append(str)
        return list(dicts.values())
