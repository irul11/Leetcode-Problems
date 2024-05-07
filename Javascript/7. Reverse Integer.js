/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    let result = ""
    
    if (x < 0) {
        result += "-"
        x *= -1
    }

    while (x > 0) {
        result += x%10
        x = Math.floor(x/10)
    }

    return result < -2147483648 || result > 2147483648-1 ? 0 : result
};