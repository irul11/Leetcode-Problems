/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function(n) {
    function rec(left, right, string) {
        if (string.length === n * 2) {
            arr.push(string);
        }

        if (left < n) {
            rec(left + 1, right, string + "(");
        }
        if (right < left) {
            rec(left, right + 1, string + ")");
        }
    }
    let arr = [];
    rec(0, 0, "");
    return arr;
};