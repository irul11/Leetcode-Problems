/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var rotate = function(matrix) {
    let n = matrix.length

    for (let i = 0; i < Math.floor(n/2); i++) {
        for (let j = i; j < n-i-1; j++) {
            let i_j = matrix[i][j],
                j_ilast = matrix[j][n - i - 1],
                jlast_i = matrix[n - j - 1][i],
                ilast_jlast = matrix[n - i - 1][n - j - 1]

            matrix[i][j] = jlast_i
            matrix[j][n - i - 1] = i_j
            matrix[n - i - 1][n - j - 1] = j_ilast
            matrix[n - j - 1][i] = ilast_jlast
        }
    }
};