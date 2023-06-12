/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {
	return function(x) {
        val = x
        for(i = functions.length - 1; i >=0 ; i--){
            val = functions[i](val)
        }
        return val
    }
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */