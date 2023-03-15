class Solution:
    def letterCombinations(self, digits: str):
        if not digits:
            return []

        letters = [
            'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz'
        ]
        result = []

        def recursion(index, currentString):
            if index == len(digits):
                result.append(currentString)
            else:
                for letter in letters[int(digits[index]) - 2]:
                    recursion(index + 1, currentString + letter)

        recursion(0, '')

        return result