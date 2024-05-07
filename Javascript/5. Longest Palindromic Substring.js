/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function(s) {
    let maxLength = 1
    let left = 0

    var checkPalindrome = function(l, r) {
        while (l >= 0 && r < s.length && s[l] === s[r]) {
            l--
            r++
        }
        if (maxLength < r-l-1) {
            maxLength = r-l-1
            left = l+1 
        }
    }

    for (let i = 0; i < s.length; i++) {
        checkPalindrome(i, i)
        checkPalindrome(i, i+1)
    }

    return s.slice(left, left + maxLength)
};
