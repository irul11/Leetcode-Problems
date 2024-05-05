/**
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidSudoku = function(board) {
    for (let r = 0; r < 9; r++) {
        let rows = new Set(),
            cols = new Set(),
            boxs = new Set()
        
        for (let c = 0; c < 9; c++) {
            let row = board[r][c],
                col = board[c][r],
                box = board[3*Math.floor(r/3) + Math.floor(c/3)][3*(r%3) + (c%3)]

            if (row !== ".") {
                if (rows.has(row)) return false
                rows.add(row)
            }
            if (col !== ".") {
                if (cols.has(col)) return false
                cols.add(col)
            }
            if (box !== ".") {
                if (boxs.has(box)) return false
                boxs.add(box)
            }
        }        
    }
    return true    
};

// isValidSudoku(
//     board = 
//         [["5","3",".",".","7",".",".",".","."]
//         ,["6",".",".","1","9","5",".",".","."]
//         ,[".","9","8",".",".",".",".","6","."]
//         ,["8",".",".",".","6",".",".",".","3"]
//         ,["4",".",".","8",".","3",".",".","1"]
//         ,["7",".",".",".","2",".",".",".","6"]
//         ,[".","6",".",".",".",".","2","8","."]
//         ,[".",".",".","4","1","9",".",".","5"]
//         ,[".",".",".",".","8",".",".","7","9"]]
// )