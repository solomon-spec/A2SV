/**
 * @param {Object | Array} obj
 * @return {boolean}
 */
var isEmpty = function(obj) {
    let count = 0
    for(let i of Object.keys(obj)){
        count += 1;
    }
    return count == 0
};