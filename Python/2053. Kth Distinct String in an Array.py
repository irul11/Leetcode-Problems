class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        distinct = []
        counter = Counter(arr)

        for i in range(len(arr)):
            if counter[arr[i]] == 1:
                distinct.append(arr[i])
        
        if k > len(distinct):
            return ''
        
        return distinct[k-1]
        