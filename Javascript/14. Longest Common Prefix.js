/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    if (strs[0] == "") return "";

    let result = ""
    let i = 0
    while (i < strs[0].length) {
        let current = strs[0][i]
        for (str of strs) {
            if (i >= str.length || str[i] != current) {
                return result;
            }
        }
        result += current
        i += 1
    }
    return result
};
