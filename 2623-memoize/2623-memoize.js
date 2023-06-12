/**
 * @param {Function} fn
 */
function memoize(fn) {
    memo = {}
    return function(...args) {
        if (!([fn,...args] in memo)) memo[[fn,...args]] = fn(...args)
        return memo[[fn,...args]]
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