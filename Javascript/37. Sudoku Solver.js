/**
 * @param {character[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */

var solveSudoku = function(board) {    

    dfs(board)
};

const dfs = function (board) {
    for (let r = 0; r < 9; r++) {
        for (let c = 0; c < 9; c++) {
            if (board[r][c] !== ".") continue;

            for (let n = 1; n < 10; n++) {                    
                if (isValid(board, r, c, ""+n)) {
                    board[r][c] = "" + n
                    if (dfs(board)) {
                        return true;
                    } else {
                        board[r][c] = ".";
                    }
                }
            }
            return false

        } 
    }
    return true
}

var isValid = function(board, r, c, n) {
    for (let i = 0; i < 9; i++) {
        if (
            board[r][i] === n ||
            board[i][c]  === n ||
            board[Math.floor(r/3)*3 + Math.floor(i/3)][Math.floor(c/3)*3 + (i%3)] === n
        ) {
            return false
        }
    }
    return true
}


// console.log(solveSudoku(
//     [[".",".","9","7","4","8",".",".","."]
//     ,["7",".",".",".",".",".",".",".","."]
//     ,[".","2",".","1",".","9",".",".","."]
//     ,[".",".","7",".",".",".","2","4","."]
//     ,[".","6","4",".","1",".","5","9","."]
//     ,[".","9","8",".",".",".","3",".","."]
//     ,[".",".",".","8",".","3",".","2","."]
//     ,[".",".",".",".",".",".",".",".","6"]
//     ,[".",".",".","2","7","5","9",".","."]]
// ))