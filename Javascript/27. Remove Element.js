/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {
	if (!nums) {
		return 0;
	}

	let k = 0;
	let slow = -1;

	for (let fast = 0; fast < nums.length; fast++) {
		if (nums[fast] !== val) {
			k += 1;
			slow += 1;
			nums[slow] = nums[fast]
		}

	}
	return k;
};