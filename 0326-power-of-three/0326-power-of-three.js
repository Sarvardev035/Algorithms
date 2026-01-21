/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfThree = function(n) {
    let i = n
    if (n <= 0) return false
    if (n === 1) return true
    do {
        i /= 3
        if (Math.floor(i) !== i || (i < 3 && i !== 1)) return false
    } while (i >= 3)
    return true
};