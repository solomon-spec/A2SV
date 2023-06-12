/**
 * @param {Function} fn
 */
function memoize(fn) {
    memo = {}
    return function(...args) {
        word = [fn,...args] 
        if (!(word in memo)) memo[word] = fn(...args)
        return memo[word]
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */