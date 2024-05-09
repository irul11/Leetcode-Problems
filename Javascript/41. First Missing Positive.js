/**
 * @param {number[]} nums
 * @return {number}
 */
var firstMissingPositive = function(nums) {
    let sets = new Set(nums)
    for (let i= 1; i < 2**31; i++) {
        if (!sets.has(i)) return i;
    }
};