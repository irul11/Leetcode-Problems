/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
	if (!nums) {
		return 0;
	}

	let k = 1;
	let slow = 0;

	for (let fast = 1; fast < nums.length; fast++) {
		if (nums[fast] !== nums[slow]) {
			k += 1;
			slow += 1;
			nums[slow] = nums[fast]
		}

	}
	return k;
};