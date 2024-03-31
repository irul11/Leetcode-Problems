/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    let area = 0;
    let left = 0;
    let right = height.length - 1;
    let temp;

    while (left < right) {
        if (height[left] > height[right]) {
            temp = height[right] * (right - left);
            right--;
        } else {
            temp = height[left] * (right - left);
            left++;
        }
        if (temp > area) {
            area = temp;
        }
    }
    return area;
};