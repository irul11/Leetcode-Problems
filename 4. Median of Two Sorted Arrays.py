class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lis = nums1 + nums2
        lis.sort()
        length = len(lis)
        if length % 2 != 0:
            return lis[(length + 1) // 2 - 1]
        else:
            return (lis[length // 2 - 1] + lis[length // 2 - 1 + 1]) / 2
