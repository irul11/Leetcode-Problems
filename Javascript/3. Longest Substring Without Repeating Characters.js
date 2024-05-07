/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let maps = new Map()
    let result = 0
    let left = 0

    for (let i = 0; i < s.length; i++) {
        if (maps.has(s[i]) && left <= maps.get(s[i])) {
            left = maps.get(s[i]) + 1 
        }
        const length = i - left + 1
        result = Math.max(result, length)
        maps.set(s[i], i)
    }
    return result
};
