class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        arr = sentence.split(" ")
        sets = set(dictionary)
        sets2 = set()
        ans = ""

        for dd in dictionary:
            for i in range(1, len(dd)):
                sets2.add(dd[:i])

        for ar in arr:
            temp = ar
            for i in range(1, len(ar)+1):
                if ar[:i] in sets:
                    temp = ar[:i]
                    break
                elif ar[:i] in sets2:
                    continue
                else:
                    break
            ans += temp + " "

        return ans [:-1]
