/**
 * @param {number} n
 * @return {number}
 */
var arrangeCoins = function(n) {
    let row = 1;
    let completed = 0;
    while (n>=row ){
        n=n-row
        row++
        completed++;

        
    }
    return completed
};