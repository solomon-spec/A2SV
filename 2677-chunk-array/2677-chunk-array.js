/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array[]}
 */
var chunk = function(arr, size) {
   let ans = [[]]
    cur = 0
    for(let num of arr){

        if (ans[cur].length < size) ans[cur].push(num)

        else{
            ans.push([num])
            cur++
        }


    }
    if(ans[0].length ===0) return []
    return ans
};

