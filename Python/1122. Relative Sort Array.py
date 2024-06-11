class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counter1 = Counter(arr1)
        ans = []
        rest = []

        for s in arr2:
            ans += [s] * counter1[s]
            del counter1[s]
        for c in counter1:
            rest += [c] * counter1[c]
        
        return ans + sorted(rest)
        