/**
 * @param {string} s
 * @return {number}
 */
var myAtoi = function(s) {
    const match = s.match(/^\s*[-+]?\d+/)
    if (!match) return 0;    
    let result = parseInt(match[0].replace(" ", ""))

    return result < -2147483648 ? -2147483648 : result > 2147483648-1 ? 2147483648-1 : result
};
