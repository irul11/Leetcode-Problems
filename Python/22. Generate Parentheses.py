class Solution:
    def generateParenthesis(self, n: int):
        def rec(left, right, string):
            if len(string) == n * 2:
                arr.append(string)
                return 

            if left < n:
                rec(left + 1, right, string + '(')

            if right < left:
                rec(left, right + 1, string + ')')

        arr = []
        rec(0, 0, '')
        return arr