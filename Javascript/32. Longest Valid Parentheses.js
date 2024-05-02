/**
 * @param {string} s
 * @return {number}
 */
var longestValidParentheses = function(s) {
    let result = 0
    let array = [-1]

    for (let i = 0; i < s.length; i++) {
        if (s[i] === "(") {
            array.push(i)
        } else {
            array.pop()
            if (array.length === 0) {
                array.push(i)
            } else {
                result = Math.max(result, i - array[array.length-1])
            }
        }
    }
    return result
};

// longestValidParentheses("))))())()()(()")