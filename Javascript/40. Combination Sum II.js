/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum2 = function(candidates, target) {
    let result = []
    candidates.sort((a,b) => a - b)
    
    let temp = []

    function backtracking(left, res) {
        if (res < 0) {
            return ;
        }
        if (res == 0) {
            result.push([...temp])
            return 
        }

        let i = left
        while (i < candidates.length) {
            temp.push(candidates[i])
            backtracking(i+1, res - candidates[i])
            temp.pop()
            let j = 1
            while (i+j < candidates.length && candidates[i] == candidates[i+j]) j++;
            i += j
        }
        return
    }

    backtracking(0, target)
    return result
};