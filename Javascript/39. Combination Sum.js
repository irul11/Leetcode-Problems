/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function(candidates, target) {
    let result = []
    let temp = []

    function backtracking(left, res) {
        // console.log(temp)
        if (res < 0) return false;
        if (res == 0) {
            result.push([...temp])
        }

        for (let i = left; i < candidates.length; i++) {
            temp.push(candidates[i])
            backtracking(i+1, res - candidates[i])
            temp.pop()
        }
    }

    backtracking(0, target)
    return result
};