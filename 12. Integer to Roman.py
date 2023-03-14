class Solution:
    def intToRoman(self, num: int) -> str:
        num_copy = num
        roman = [
            'I', 'V', 'X', 'L', 'C', 'D', 'M'
        ]
        indeks = 0
        result = ''

        while indeks <= 6:
            mod = num_copy % 10
            num_copy //= 10
            if (mod == 0):
                pass
            elif (mod <= 3):
                result = roman[indeks] * mod + result
            elif (mod == 4):
                result = roman[indeks] + roman[indeks + 1] + result
            elif (mod == 9):
                result = roman[indeks] + roman[indeks + 2] + result
            else:
                result = roman[indeks + 1] + roman[indeks] * (mod - 5) + result
            if num_copy == 0:
                break
            indeks += 2
            print(num_copy)

        return result