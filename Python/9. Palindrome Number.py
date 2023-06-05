class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        if (string[::-1] != string):
            return False
        return True