class Solution(object):
    def isValid(self, s):
        arr = []
        for letter in s:
            if letter == "(" or letter == "[" or letter == "{":
                arr.append(letter)
            else:
                if len(arr) == 0:
                    return False
                if letter ==")" and arr[-1] == "(":
                    arr.pop()
                elif letter =="]" and arr[-1] == "[":
                    arr.pop()
                elif letter =="}" and arr[-1] == "{":
                    arr.pop()
                else:
                    return False
                        
        return not arr