/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permute = function(nums) {
    let result = []
    var heapPerm = function(nums, size) {
        if (size == 1) {
            result.push([...nums])
        }

        for (let i = 0; i < size; i++) {
            heapPerm(nums, size-1)

            if (size % 2 == 0) {
                temp = nums[i]
                nums[i] = nums[size-1]
                nums[size-1] = temp
            } else {
                temp = nums[0]
                nums[0] = nums[size-1]
                nums[size-1] = temp
            }
        }
    }
    heapPerm(nums, nums.length)
    return result
};

