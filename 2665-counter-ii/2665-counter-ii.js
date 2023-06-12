/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    def = init
    const obj = {
        increment: () => ++init,
        decrement: () => --init,
        reset: () => {
            init = def
            return init
        }
    }
    return obj
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */