class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        arr = [(heights[i], names[i]) for i in range(len(names))]

        arr.sort(reverse=True)

        return list(map(lambda x: x[1], arr))
