class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums, 0, len(nums)-1)

        return nums

    def mergeSort(self, arr, start, end):
        if start >= end:
            return
            
        mid = (start + end) // 2
        self.mergeSort(arr, start, mid)
        self.mergeSort(arr, mid + 1, end)
        self.merge(arr, start, mid, end)
    
    def merge(self, arr, start, mid, end):
        leftArr = []
        rightArr = []

        for i in range(mid - start + 1):
            leftArr.append(arr[start+i])
        
        for i in range(end - mid):
            rightArr.append(arr[mid+1+i])
        # print(leftArr, rightArr)
        indexLeft = indexRight = 0

        while indexLeft < len(leftArr) and indexRight < len(rightArr):
            if leftArr[indexLeft] <= rightArr[indexRight]:
                arr[start] = leftArr[indexLeft]
                indexLeft += 1
            else:
                arr[start] = rightArr[indexRight]
                indexRight += 1
            start += 1
        
        while indexLeft < len(leftArr):
            arr[start] = leftArr[indexLeft]
            indexLeft += 1
            start += 1
        
        while indexRight < len(rightArr):
            arr[start] = rightArr[indexRight]
            indexRight += 1
            start += 1

        del leftArr
        del rightArr

