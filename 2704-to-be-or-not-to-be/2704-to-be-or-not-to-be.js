/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {
    const ob = {
        toBe:(cur)=> {
            if(val === cur) return true
            throw "Not Equal"},
        notToBe: (cur) => {
            if(val !== cur)return true
            throw "Equal"}}
    return ob
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */