/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    let maps = new Map()
    
    for (str of strs) {
        let sorted = str.split('').sort().join('')
        
        if (maps.has(sorted)) {
            let temp = maps.get(sorted)
            temp.push(str)
            maps.set(sorted, temp)
        } else {
            maps.set(sorted, [str])
        }
    }

    return Array.from(maps.values())
};
