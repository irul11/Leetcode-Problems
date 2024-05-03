/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
const searchRange = function(nums, target) {
    let left = binarySearch(nums, target, true)
    let right = left != -1 ? binarySearch(nums, target, false) : -1
    return [left, right]
};

const binarySearch = function(nums, target, toLeft) {
    index = -1
    let left = 0
    let right = nums.length - 1
    
    while (left <= right) {
        let mid = Math.floor((left + right) / 2)
        if (target > nums[mid]) {
            left = mid + 1
        } else if (target < nums[mid]) {
            right = mid - 1
        } else {
            index = mid
            if (toLeft) {
                right = mid - 1
            } else {
                left = mid + 1
            }
        }
    }
    return index
}

// searchRange(
//     [],
//     0
// )