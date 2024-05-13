/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var threeSumClosest = function(nums, target) {
    let n = nums.length
    nums.sort((a,b) => a-b)
    let result = Infinity

    for (let i = 0; i < n-2; i++) {
        if (i > 0 && nums[i] == nums[i-1]) continue;

        let left = i + 1
        let right = n - 1
        while (left < right) {
            let total = nums[i] + nums[left] + nums[right]
            
            if (Math.abs(result-target) > Math.abs(total-target)) {
                result = total
            }
            if (total > target) {
                right--
            } else if (total < target) {
                left++
            } else {
                return target
            }
        }
    }
    return result
};
