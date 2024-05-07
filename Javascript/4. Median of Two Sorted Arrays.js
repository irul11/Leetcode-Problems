/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
    let totalLength = nums1.length + nums2.length
    let i1 = 0
    let i2 = 0
    let mid = Math.floor(totalLength/2) + 1
    
    let curr = 0
    let prev = 0

    for (let i = 0; i < mid; i++) {
        prev = curr
        if (i1 >= nums1.length && i2 >= nums2.length) {
            return 0
        } else if (i2 >= nums2.length || nums1[i1] <= nums2[i2]) {
            curr = nums1[i1]
            i1++
        } else {
            curr = nums2[i2]
            i2++
        }
    }

    return totalLength % 2 != 0 ? curr : (curr+prev)/2
};