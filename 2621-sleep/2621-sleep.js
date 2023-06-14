/**
 * @param {number} millis
 */
async function sleep(millis) {
    res = new Promise((resolve,reject)=>{
    setTimeout(()=>{ resolve()},millis)
    })
    return res
    
}

/** 
 * let t = Date.now()
 * sleep(100).then(() => console.log(Date.now() - t)) // 100
 */