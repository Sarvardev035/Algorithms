/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {

 let [ a,b] = [1,1];
    while(n-->1) [ a , b] =[b  , a + b];
    
    return b

 
};