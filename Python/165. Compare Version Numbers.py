class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        arr1 = version1.split(".")
        arr2 = version2.split(".")

        if len(arr1) < len(arr2):
            arr1 += ["0"] * (len(arr2) - len(arr1))
        elif len(arr1) > len(arr2):
            arr2 += ["0"] * (len(arr1) - len(arr2))

        for i in range(len(arr1)):
            if int(arr1[i]) > int(arr2[i]):
                return 1
            elif int(arr1[i]) < int(arr2[i]):
                return -1

        return 0
        