class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        temp = ""

        for i in range(len(word)):
            temp = word[i] + temp
            if word[i] == ch:
                return temp + word[i+1:]
        return word
        