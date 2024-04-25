/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var nextPermutation = function(nums) {
    let right = nums.length - 1
    let left = right - 1

    while (left >= 0) {
        if (nums[left] < nums[left+1]) {
            while (nums[right] <= nums[left]) {
                right--
            }
            const temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp
            break
        }
        left--
    }

    right = nums.length - 1
    left++
    while (left < right) {
        const temp = nums[left]
        nums[left] = nums[right]
        nums[right] = temp
        left++
        right--
    }
    console.log(nums)
};

nextPermutation(
    [1,2,5,4,3,2,1]
)