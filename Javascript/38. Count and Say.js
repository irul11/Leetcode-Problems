/**
 * @param {number} n
 * @return {string}
 */
var countAndSay = function(n) {
    if (n === 1) return "1";
    return rle(countAndSay(n-1))
};

var rle = function(str) {
    let count = 0
    let curr = str.charAt(0)
    let temp = ""

    for (let s = 0; s < str.length; s++) {
        if (curr === str.charAt(s)) {
            count++
        } else {
            temp += `${count}${curr}`
            count = 1
            curr = str.charAt(s)
        }
    }
    temp += `${count}${curr}`
    return temp
}