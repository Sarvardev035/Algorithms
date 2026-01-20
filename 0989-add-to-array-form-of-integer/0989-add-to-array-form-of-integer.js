/**
 * @param {number[]} num
 * @param {number} k
 * @return {number[]}
 */
var addToArrayForm = function(num, k) {
    let i = num.length - 1;
    let carry = 0;
    let result = [];

    while (i >= 0 || k > 0 || carry > 0) {
        let digitNum = i >= 0 ? num[i] : 0;
        let digitK = k % 10;

        let sum = digitNum + digitK + carry;
        result.push(sum % 10);
        carry = Math.floor(sum / 10);

        i--;
        k = Math.floor(k / 10);
    }

    result.reverse();
    return result;
};
