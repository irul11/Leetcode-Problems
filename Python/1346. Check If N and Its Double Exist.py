class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        sets = set()
        for i in range(len(arr)):
            if arr[i] * 2 in sets or (arr[i] % 2 == 0 and arr[i] // 2 in sets):
                return True
            sets.add(arr[i])
        return False
        