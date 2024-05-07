/**
 * @param {string} s
 * @param {string} p
 * @return {boolean}
 */
var isMatch = function(s, p) {    
    const cache = {}

    var dfs = function(i, j) {
        if (cache.hasOwnProperty(`i${i}j${j}`)) return cache[`i${i}j${j}`];

        if (i >= s.length && j >= p.length) return true;
        if (j >= p.length) return false;

        const match = i < s.length && (s[i] === p[j] || p[j] === ".")

        if (j+1 < p.length && p[j+1] === "*") {
            cache[`i${i}j${j}`] = dfs(i, j+2) || (match && dfs(i+1, j))
            return cache[`i${i}j${j}`];
        }

        cache[`i${i}j${j}`] = match ? dfs(i+1, j+1) : false

        return cache[`i${i}j${j}`]
    }
    return dfs(0,0)
};