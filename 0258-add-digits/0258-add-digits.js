/**
 * @param {number} num
 * @return {number}
 */
var addDigits = function(num) {
    while(num>=10)
    {
        let sum = 0;
        let s= num.toString();

        for(let i=0; i<s.length; i++){
            sum += Number(s[i]);
        }
        num=sum
    }
    return num;
};