/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    let n = nums.length
    let result = []
    nums.sort((a,b) => a - b)

    for (let i = 0; i < n-2; i++) {
        if (i > 0 && nums[i] == nums[i-1]) continue;

        let left = i + 1
        let right = n - 1
        while (left < right) {
            let total = nums[i] + nums[left] + nums[right]
            if (total > 0) {
                right--
            } else if (total < 0) {
                left++
            } else {
                result.push([nums[i], nums[left], nums[right]])
                left++
                while (left < right && nums[left] == nums[left-1]) {
                    left++
                }
            }
        }
    }
    return result
};
