class Solution:
    maps = {
        1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven",
        8:"Eight", 9:"Nine", 10:"Ten", 11:"Eleven", 12:"Twelve", 13:"Thirteen",
        14:"Fourteen", 15:"Fifteen", 16:"Sixteen", 17:"Seventeen", 18:"Eighteen",
        19:"Nineteen", 20:"Twenty", 30:"Thirty", 40:"Forty", 50:"Fifty", 60:"Sixty",
        70:"Seventy", 80:"Eighty", 90:"Ninety"        
    }
    arr = [" ", " Thousand ", " Million ", " Billion ", " Trillion "]

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        ans = ""
        i = 0
        while num > 0:
            if num%1000 != 0:
                ans = self.threeDigits(num%1000) + self.arr[i] + ans
            num //= 1000
            i += 1
        return ans.strip()
    
    def threeDigits(self, digits: int) -> str:
        res = ""
        helper = [" ", " ", " Hundred "]
        i = 0
        
        while digits > 0:
            if i == 0 and 10 <= digits % 100 <= 19:
                res = self.maps[digits%100] + res
                digits //= 100
                i += 2
            elif digits%10 in self.maps:
                if i == 1:
                    res = self.maps[digits*10%100] + helper[i] + res
                else:
                    res = self.maps[digits%10] + helper[i] + res
                digits //= 10
                i += 1
            else:
                digits //= 10
                i += 1
        return res.strip()
