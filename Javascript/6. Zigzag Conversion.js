/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
var convert = function(s, numRows) {
    if (numRows <= 1) {
        return s;
    }
    let step = 1 + (numRows-2)*2
    let result = ""
    
    for (let n=0; n < numRows; n++) {
        let tempStep = step - 2*n
        for (let i=0; i<s.length; i += step+1) {
            if (!s[i+n]) break
            temp = s[i+n] 
            result += temp
            if (tempStep !== step && tempStep > 0) {
                if (!s[i+n+tempStep+1]) break
                temp = s[i+n+tempStep+1]
                result += temp
            }
        }
    }
    return result
};