class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        if len(nums1) <= len(nums2):
            counter = Counter(nums1)
            for n in nums2:
                if n in counter and counter[n] > 0:
                    ans.append(n)
                    counter[n] -= 1
        else:
            counter = Counter(nums2)
            for n in nums1:
                if n in counter and counter[n] > 0:
                    ans.append(n)
                    counter[n] -= 1
        
        return ans
        