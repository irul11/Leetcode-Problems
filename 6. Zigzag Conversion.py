class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        gap = numRows - 2
        double = numRows + gap
        text = ''
        for i in range(numRows):
            index = i
            while index < len(s):
                if i != 0 and i != numRows - 1:
                    if index + double > len(s) - 1:
                        text += s[index]
                    else:
                        text += s[index] + s[index + double]
                else:
                    text += s[index]
                index += numRows + gap
            double -= 2
        return text