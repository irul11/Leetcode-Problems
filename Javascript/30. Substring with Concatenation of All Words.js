/**
 * @param {string} s
 * @param {string[]} words
 * @return {number[]}
 */
var findSubstring = function(s, words) {
    const counterWords = {}
    for (word of words) {
        if (counterWords[word]) {
            counterWords[word]++
        } else {
            counterWords[word] = 1
        }
    }
    
    const lengthWords = words.length
    const lengthElement = words[0].length
    const lengthS = s.length
    const result = []

    for (i=0; i < lengthElement; i++) {
        let counterTemp = {}
        let left = i
        let right = i
        let t = 0
        while (right + lengthElement <= lengthS) {
            let word = s.slice(right, right + lengthElement)
            right += lengthElement
            if (!counterWords[word]) {
                left = right
                counterTemp = {}
                t = 0
                continue
            }

            if (counterTemp[word]) {
                counterTemp[word]++
            } else {
                counterTemp[word] = 1
            }
            t++
            
            while (counterTemp[word] > counterWords[word]) {
                let removeWord = s.slice(left, left + lengthElement)
                left += lengthElement
                counterTemp[removeWord]--
                t--
            }

            if (t == lengthWords) {
                result.push(left)
            }
        }
    }
    console.log(result)
    return result;
};

findSubstring(
    "lingmindraboofooowingdingbarrbarrwingmonkeypoundcake",
    ["fooo","barr","wing","ding","wing"]
)