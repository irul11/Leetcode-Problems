class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        count = [0] * 26
        letters_count = [0] * 26

        for l in letters:
            count[ord(l) - ord('a')] += 1
        
        self.ans = 0
        self.backtracking(words, score, count, letters_count, 0, 0)
        return self.ans

    def backtracking(self, words: List[str], score: List[int], count: List[int], letters_count: List[int], pos: int, temp: int):
        for i in range(26):
            if letters_count[i] > count[i]:
                return
        
        self.ans = max(self.ans, temp)
        for i in range(pos, len(words)):
            for w in words[i]:
                letters_count[ord(w) - ord('a')] += 1
                temp += score[ord(w) - ord('a')]
            self.backtracking(words, score, count, letters_count, i + 1, temp)
            for w in words[i]:
                letters_count[ord(w) - ord('a')] -= 1
                temp -= score[ord(w) - ord('a')]
                