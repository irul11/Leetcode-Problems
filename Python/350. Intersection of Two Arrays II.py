class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        counter = Counter(nums1)
        
        for n in nums2:
            if n in counter and counter[n] > 0:
                ans.append(n)
                counter[n] -= 1

        return ans
        