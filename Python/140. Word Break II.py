class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        return self.helper(s, 0, word_set)
    
    def helper(self, s: str, left: int, word_set: set) -> List[str]:
        valid = []

        if left == len(s):
            valid.append("")
        
        for i in range(left+1, len(s)+1):
            prefix = s[left:i]
            if prefix in word_set:
                suffix = self.helper(s, i, word_set)
                for suff in suffix:
                    if suff == "":
                        valid.append(prefix + "" + suff)
                    else:
                        valid.append(prefix + " " + suff)
        return valid
