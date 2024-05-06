/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const seen = new Map()
    for (let i = 0; i < nums.length; i++) {        
        const remaining = target - nums[i]
        if (seen.has(remaining)) {
            return [i, seen.get(remaining)]
        }
        seen.set(nums[i], i)
    }
};
