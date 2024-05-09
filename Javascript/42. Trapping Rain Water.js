/**
 * @param {number[]} height
 * @return {number}
 */
var trap = function(height) {
    let left = Array()
    
    let n = height.length
    let result = 0

    for (let i = 0; i < n; i++) {
        if (left.length > 0 && height[i] >= left[left.length-1][1]) {
            let right = [i, height[i]]
            let temp = left.pop()[1]
            while (left.length && left[left.length-1][1] <= right[1]) {
                let l = left.pop()
                result += ( (l[1]-temp) * (i-l[0]-1) )
                temp = l[1]
            }
            if (left.length > 0 && left[left.length-1][1] >= right[1]) {
                result += ( (right[1]-temp) * (right[0]-left[left.length-1][0]-1) )
            }
        }
        left.push([i, height[i]])
    }
    return result
};