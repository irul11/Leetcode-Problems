/**
 * @param {string} s
 * @param {string} p
 * @return {boolean}
 */
var isMatch = function(s, p) {
    let i = 0
    let j = 0

    let lastMatch = 0
    let star = -1

    while (i < s.length) {
        if (j < p.length && (s[i] == p[j] || p[j] == "?")) {
            i++
            j++
        } else if (j < p.length && p[j] == "*") {
            last_match = i
            star = j
            j++
        } else if (star != -1) {
            j = star + 1
            i = last_match + 1
            last_match++
        } else {
            return false
        }
    }

    while (j < p.length && p[j] == "*") {
        j++
    }

    return j == p.length
};