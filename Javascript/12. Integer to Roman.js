/**
 * @param {number} num
 * @return {string}
 */
var intToRoman = function(num) {
    let numCopy = num
    let roman = [
        'I', 'V', 'X', 'L', 'C', 'D', 'M'
    ]
    let index = 0
    let result = ''

    while (index <= 6) {
        let mod = numCopy % 10
        numCopy = Math.floor(numCopy/10)

        if (mod == 0) {
        } else if (mod <= 3) {
            result = roman[index].repeat(mod) + result
        } else if (mod == 4) {
            result = (roman[index] + roman[index + 1]) + result
        } else if (mod == 9) {
            result = (roman[index] + roman[index + 2]) + result
        } else {
            result = (roman[index + 1] + roman[index].repeat(mod-5)) + result
        }
        index += 2
    }
    return result
};
