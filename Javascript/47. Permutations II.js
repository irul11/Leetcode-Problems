/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permuteUnique = function(nums) {
    return backtrack(0, nums, [])
};

var backtrack = function(s, nums, ans) {
    if (s == nums.length) {
        ans.push([...nums])
        return ans
    }
    
    let sets = new Set()
    for (let i = s; i < nums.length; i++) {
        if (!sets.has(nums[i])) {
            sets.add(nums[i])
            temp = nums[i]
            nums[i] = nums[s]
            nums[s] = temp

            ans = backtrack(s+1, nums, ans)
            
            temp = nums[i]
            nums[i] = nums[s]
            nums[s] = temp
        }
    }
    return ans
}
