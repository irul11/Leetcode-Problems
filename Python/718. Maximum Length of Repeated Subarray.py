class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        #  Using rolling hash
        n = len(nums1)
        m = len(nums2)

        r = min(n,m)
        l  = 0

        def helper(mid):

            hashset1 = set()
            hashset2 = set()
            base = 101
            mod = 2**32

            a = pow(base, mid, mod)

            curhash = 0 
            for i in range(n):

                curhash = curhash * base + nums1[i]

                if i>=mid:
                    curhash -= nums1[i-mid] * a
                
                curhash %= mod

                if i >= mid-1:
                    hashset1.add(curhash)
            
            curhash = 0
            for j in range(m):
                curhash = curhash * base + nums2[j]

                if j>= mid:
                    curhash -= nums2[j-mid] * a
                curhash %= mod

                if j >= mid-1:
                    hashset2.add(curhash)
            
            return len(hashset1.intersection(hashset2)) > 0

        while l < r:

            mid = l + (r-l+1) // 2

            if helper(mid):
                l = mid 
            else:
                r = mid -1
        return l

