/**
 * @param {number} dividend
 * @param {number} divisor
 * @return {number}
 */
var divide = function(dividend, divisor) {
    if (dividend === -2147483648 && divisor === -1) {
        return 2147483647;
    }

    let a = Math.abs(dividend),
        b = Math.abs(divisor),
        result = 0;
    
    while (a >= b) {
        let count = 1;
        let baseDivisor = b;
        while (baseDivisor <= (a >> 1)) {
            baseDivisor <<= 1;
            count <<= 1;
        }
        result += count;
        a -= baseDivisor;
    }

    return ((dividend >= 0) === (divisor >= 0)) ? result : -result;
};